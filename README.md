# Real-Time Vehicle Detection & Gate Control Simulation

This project is a Python application that uses the YOLOv4-tiny model with OpenCV's DNN module to perform real-time vehicle detection in a video stream. It features a multithreaded architecture to ensure a responsive user interface while processing video, and simulates a gate control system based on vehicle detection states.

## Screenshots

<table>
  <tr>
    <td><img src="https://github.com/onurmertanarat/DetectVehuman/blob/main/assets/detectvehuman.gif" alt="Vehicle Detection"></td>
    <td><img src="https://github.com/onurmertanarat/DetectVehuman/blob/main/assets/detectvehuman-log.gif" alt="Log Viewer"></td>
  </tr>
</table>

---

## Architecture

This application is built with a clean, modular architecture, separating different responsibilities into distinct classes:

* **`main.py`**: The main entry point and orchestrator that initializes and coordinates all components.
* **`YOLOVehicleDetector`**: The core engine responsible for all video processing, deep learning inference (YOLOv4), object detection, and state management for the gate logic.
* **`LogSystem`**: A dedicated class for handling all event logging using Python's standard `logging` module.
* **`LogViewer`**: A `Tkinter`-based GUI application that displays the logs from the `LogSystem` and the current status of the gate in real-time.
* **Multithreading**: The heavy video processing runs on a separate background thread, while the Tkinter GUI runs on the main thread. This ensures the user interface remains smooth and responsive at all times.

---

## Features

* **Real-Time Object Detection:** Utilizes the YOLOv4-tiny model to detect cars and trucks with high efficiency.
* **GPU Acceleration:** Automatically detects and uses a CUDA-enabled GPU if available, falling back to the CPU if not.
* **Multithreaded & Responsive GUI:** A non-blocking architecture that provides a smooth user experience.
* **Stateful Tracking Logic:** Implements a simple state machine to track when a vehicle is "entering" or "exiting" the frame, simulating the logic for an automated gate.
* **Professional Logging:** All significant events (vehicle detection, gate status change, errors) are timestamped and logged to a file.
* **Object-Oriented Design:** Clean, modular, and scalable code structure based on the Single Responsibility Principle.

---

## Technology Stack

* Python 3
* OpenCV (`opencv-python`) for video processing and DNN inference.
* Tkinter for the graphical user interface.
* Git LFS for managing the large model weights file.

---

## Setup and Usage

### Prerequisites

* Python 3.8+
* pip
* Git
* Git LFS (one-time setup)

### Installation

1.  **Set up Git LFS (if you haven't already):**
    ```sh
    git lfs install
    ```

2.  **Clone the repository:**
    ```sh
    git clone [https://github.com/onurmertanarat/DetectVehuman.git](https://github.com/onurmertanarat/DetectVehuman.git)
    cd DetectVehuman
    ```
    *(Git LFS will automatically download the `.weights` model file during the clone process.)*

3.  **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

4.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

Simply run the main script from the terminal:

```sh
python main.py
```

This will launch two windows: the Tkinter GUI showing logs and the OpenCV window showing the live vehicle detection. Press 'q' on the OpenCV window to quit.

---

## Contact

Onur Mert Anarat

[linkedin.com/in/onurmertanarat](https://www.linkedin.com/in/onurmertanarat)
