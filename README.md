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
- NumPy (`numpy`)
- YOLOv4 Pre-Trained Weights

## How It Works

- YOLOv4 Model: The YOLOv4 model is used to detect objects (in our case, balls) within each frame of the video.
- Ball Detection: Each frame is passed through the YOLOv4 model, which outputs bounding boxes and confidence scores for all detected objects. If a ball is detected (typically labeled as "sports ball" in the class list), its position is tracked.
- Tracking: The tracked ball's movement is visualized in the output video by drawing bounding boxes on the ball and arrow show the ball movment as it moves from frame to frame.
- Output: A video is generated showing the tracking results, where the ball's position is marked with bounding boxes and arrow show its movement.

## Demo

https://github.com/user-attachments/assets/28c5e5da-22fe-4a8c-8393-bc31b41294ce



## Contributing

Feel free to contribute to this project by submitting issues, improvements, or feature requests. If you have any enhancements or bug fixes, please submit a pull request.

## Acknowledgements
- YOLOv4 for object detection.
- OpenCV for video processing.
- Python community for supporting open-source development.
