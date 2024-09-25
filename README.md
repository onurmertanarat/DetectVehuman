# DetectVehuman (Detect Vehicle and Human)
This project detects vehicles and controls gate lock based on vehicle presence using YOLOv4-Tiny. It includes a GUI to monitor gate status and logs system events.


## Features
- Real-time vehicle detection using YOLOv4-Tiny.
- Logs system events for vehicle entry/exit.
- A GUI to visualize logs and gate status.


## Requirements
- Python 3.x
- OpenCV
- NumPy


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/detect_vehuman.git

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt


## Usage
To start the vehicle detection system:
    
    python main.py


## Images
   ![YOLO Detection](https://github.com/onurmertanarat/DetectVehuman/blob/main/imgs/vehicle_detection.png)
   
   ![Log Viewer](https://github.com/onurmertanarat/DetectVehuman/blob/main/imgs/log.png)


## License

```txt
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
2. The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement.

**Commercial use of this software is prohibited without prior permission from the author. For commercial inquiries, please contact [Onur Mert Anarat] at your.anaratonurmert@yandex.com.**
