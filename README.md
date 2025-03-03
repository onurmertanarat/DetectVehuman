# DetectVehuman (Detect Vehicle and Human)

## Overview
DetectVehuman is a real-time vehicle detection system using **YOLOv4-Tiny**. It monitors vehicle presence, controls gate locks, and provides a **GUI** to track system events.

## Features
- **Real-time vehicle detection** with YOLOv4-Tiny.
- **Automated gate control** based on vehicle presence.
- **Event logging** for vehicle entry/exit.
- **User-friendly GUI** to monitor logs and gate status.

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/detect_vehuman.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start the detection system, run:
```bash
python main.py
```

## Screenshots
![YOLO Detection](https://github.com/onurmertanarat/DetectVehuman/blob/main/imgs/vehicle_detection.png)

![Log Viewer](https://github.com/onurmertanarat/DetectVehuman/blob/main/imgs/log.png)

## License
This project is licensed under the **MIT License**.

**Note:** Commercial use of this software is **prohibited** without prior permission from the author.
