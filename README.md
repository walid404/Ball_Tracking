# Ball Tracking Video Using YOLOv4 Pre-Trained Model

## Overview

Welcome to the **Ball Tracking Video** project, where we utilize the power of **YOLOv4**, one of the most advanced real-time object detection models, to track the movement of a ball in a video. This repository provides a simple solution to automatically detect and track the ball in various video sequences using a pre-trained YOLOv4 model.

By leveraging YOLOv4, we achieve fast and accurate detection, ensuring smooth real-time tracking of moving balls in sports videos, games, or any environment where a spherical object is the primary subject.

---

## Features

- **Real-Time Object Detection**: Use YOLOv4 pre-trained weights to detect balls in the video frames.
- **Ball Tracking**: Track the ball's movement across frames with precision.
- **High Performance**: Efficient processing using a powerful object detection algorithm (YOLOv4).
- **Pre-trained Model**: No need to train the model; simply use the pre-trained YOLOv4 weights for detection.
- **Supports Custom Videos**: The script works with any input video file for tracking ball movement.

---

## Requirements

Before running the project, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`opencv-python`)
- PIL (`Pillow`)
- NumPy (`numpy`)
- [YOLOv4 Pre-Trained Weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights).

  You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

---
## Setup and Usage
1. Clone the repository:
     ```bash
     git clone https://github.com/yourusername/ball-tracking-video-yolov4.git
     cd ball-tracking-video-yolov4
     ```
2. Download YOLOv4 Pre-Trained Weights:
     You can download the YOLOv4 weights from the official [YOLO repo](https://github.com/AlexeyAB/darknet) or from this direct [link](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights).
     Place the yolov4.weights file in the model directory of the project.
3. Run the Ball Tracking Script:
   Once the setup is complete, run the following Python script to start ball tracking:

```bash
python track_ball.py

```

4. Then go to Web Application and use it with your input video.


---



## How It Works

- YOLOv4 Model: The YOLOv4 model is used to detect objects (in our case, balls) within each frame of the video.
- Ball Detection: Each frame is passed through the YOLOv4 model, which outputs bounding boxes and confidence scores for all detected objects. If a ball is detected (typically labeled as "sports ball" in the class list), its position is tracked.
- Tracking: The tracked ball's movement is visualized in the output video by drawing bounding boxes on the ball and arrow show the ball movment as it moves from frame to frame.
- Output: A video is generated showing the tracking results, where the ball's position is marked with bounding boxes and arrow show its movement.

---

## Demo


https://github.com/user-attachments/assets/a73bdd55-a60c-416b-b8cd-ba6d10bee376


---

## APP
![image](https://github.com/user-attachments/assets/c3a26783-613a-48c3-ae7f-e81b648a6ed9)

---

## Contributing

Feel free to contribute to this project by submitting issues, improvements, or feature requests. If you have any enhancements or bug fixes, please submit a pull request.

---

## Acknowledgements
- YOLOv4 for object detection.
- OpenCV for video processing.
- Python community for supporting open-source development.
