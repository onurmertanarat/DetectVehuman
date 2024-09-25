import cv2
import numpy as np
import os

class YOLOVehicleDetector:
    def __init__(self, video_path, yolo_cfg, yolo_weights, coco_names, log_system, gui, confidence_threshold=0.6):
        self.net = None
        self.vehicle_detected = False
        self.vehicle_state = None
        self.vehicle_exit_time = None
        self.gate_lock_delay = 5
        self.consecutive_vehicle_frames = 0
        self.frame_count_threshold = 5
        self.log_system = log_system
        self.gui = gui
        self.cap = None
        self.running = True
        self.confidence_threshold = confidence_threshold

        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video dosyası bulunamadı: {video_path}")
        if not os.path.exists(yolo_cfg) or not os.path.exists(yolo_weights):
            raise FileNotFoundError(f"YOLO yapılandırma dosyaları eksik: {yolo_cfg}, {yolo_weights}")
        if not os.path.exists(coco_names):
            raise FileNotFoundError(f"COCO isim dosyası bulunamadı: {coco_names}")

        try:
            self.net = cv2.dnn.readNetFromDarknet(yolo_cfg, yolo_weights)
        except Exception as e:
            raise RuntimeError(f"YOLO modeli yüklenirken bir hata oluştu: {e}")

        if cv2.cuda.getCudaEnabledDeviceCount() > 0:
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        else:
            self.log_system.log_event("CUDA mevcut değil, CPU kullanılacak.")

        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]

        with open(coco_names, "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

        self.video_path = video_path

    def detect_vehicles(self, frame):
        frame = cv2.resize(frame, (640, 480))
        height, width, _ = frame.shape

        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        boxes = []
        confidences = []
        class_ids = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > self.confidence_threshold and class_id in [2, 7]:  # Class IDs for car and truck
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, 0.3)

        if len(indices) > 0:
            indices = indices.flatten()

        vehicle_present = False
        for i in indices:
            x, y, w, h = boxes[i]
            label = str(self.classes[class_ids[i]])
            confidence = confidences[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {int(confidence * 100)}%", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 0), 2)
            vehicle_present = True

        current_time = cv2.getTickCount() / cv2.getTickFrequency()

        if vehicle_present:
            if self.vehicle_state is None:
                self.vehicle_state = 'entering'
                self.log_system.log_event("Araç algılandı, kapı kilitlendi.")
                self.gui.update_gate_status("Kilitle")
        else:
            if self.vehicle_state == 'entering':
                self.vehicle_state = 'exiting'
                self.vehicle_exit_time = current_time
            elif self.vehicle_state == 'exiting':
                if self.vehicle_exit_time and (current_time - self.vehicle_exit_time) > self.gate_lock_delay:
                    self.vehicle_state = None
                    self.log_system.log_event("Araç çıkışı tespit edildi, kapı açıldı.")
                    self.gui.update_gate_status("Açık")

        return frame

    def process_video(self):
        try:
            self.cap = cv2.VideoCapture(self.video_path)
            if not self.cap.isOpened():
                raise IOError(f"Video dosyası açılırken bir hata oluştu: {self.video_path}")

            while self.cap.isOpened() and self.running:
                ret, frame = self.cap.read()
                if not ret:
                    break

                processed_frame = self.detect_vehicles(frame)

                cv2.imshow('Vehicle Detection', processed_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False

            self.cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            self.log_system.log_event(f"Video işleme sırasında bir hata oluştu: {e}")
            if self.cap is not None:
                self.cap.release()
            cv2.destroyAllWindows()

    def stop(self):
        self.running = False
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()
