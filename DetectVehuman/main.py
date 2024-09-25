import tkinter as tk
import threading
from log_system import LogSystem
from log_viewer import LogViewer
from yolo_vehicle_detector import YOLOVehicleDetector

def main():
    video_path = "videos/traffic1.mp4"
    yolo_cfg = "models/yolov4-tiny.cfg"
    yolo_weights = "models/yolov4-tiny.weights"
    coco_names = "models/coco.names"

    log_system = LogSystem()

    root = tk.Tk()
    log_viewer = LogViewer(root)

    def run_gui():
        root.mainloop()

    try:
        detector = YOLOVehicleDetector(video_path, yolo_cfg, yolo_weights, coco_names, log_system, log_viewer)
    except Exception as e:
        print(f"YOLO Detector başlatılamadı: {e}")
        return

    video_thread = threading.Thread(target=detector.process_video, daemon=True)
    video_thread.start()

    def on_closing():
        detector.stop()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    run_gui()

    video_thread.join()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
