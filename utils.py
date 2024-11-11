import cv2
import numpy as np
from PIL import Image
import imageio

# Load YOLO model
yolo_net = cv2.dnn.readNet("model/yolov4.weights", "model/yolov4.cfg")  # Replace with your path to weights and config
layer_names = yolo_net.getLayerNames()
output_layers = [layer_names[i - 1] for i in yolo_net.getUnconnectedOutLayers()]

# Load class labels
with open("model/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

def detect_ball(x1, y1, img):

    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    yolo_net.setInput(blob)
    layer_outputs = yolo_net.forward(output_layers)

    # Initialize lists for detected boxes, confidences, and class IDs
    boxes = []
    confidences = []
    class_ids = []

    # Process detections
    for out in layer_outputs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Only consider "sports ball" class (class_id = 32 in coco.names)
            if confidence > 0.8 and class_id == 32:
                # Get bounding box coordinates
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Add bounding box to list
                boxes.append([center_x - w // 2, center_y - h // 2, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Maximum Suppression (NMS)
    indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)

    # Draw final bounding boxes after NMS
    if len(indices) > 0:
        for i in indices.flatten():  # Flatten the array returned by NMS
            x, y, w, h = boxes[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Ball", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        if x1 != None and x != None and y1 != None and y != None:
            # Calculate displacement
            dx = int(x) - int(x1)
            dy = int(y) - int(y1)
            cv2.putText(img, "X Changed By: " + str(dx), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(img, "Y Changed By: " + str(dy), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            print(f"Ball moved by ({dx}, {dy})")
            arrow_thickness = 3  # Increase thickness of the line
            arrow_color = (0, 0, 255)  # Red color for the arrow
            tip_length = 0.1  # Make the tip of the arrow more prominent
            x += int(0.5 * w)
            y += int(0.5 * h)
            cv2.arrowedLine(img, (x1, y1), (x, y), arrow_color, arrow_thickness, tipLength=tip_length)

        return img, x, y
    else:
        print("Ball not detected")
        return None, None, None


def create_video(images, fps, output_video_path):
    # Ensure there are images to process
    if not images:
        raise Exception("No valid frames to create video.")

    # Read the first image to get the size (assuming all images have the same size)
    frame = images[0]
    height, width, channels = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 format
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Loop through images and add them to the video
    for image in images:
        # Ensure the image is in the correct type and size
        image = np.uint8(image)  # Ensure the image is in uint8 format
        image = cv2.resize(image, (width, height))  # Resize if necessary
        video_writer.write(image)

    # Release the VideoWriter object and finalize the video file
    video_writer.release()

    print(f"Video saved to {output_video_path}")

def create_video_pil(images, fps, output_video_path):
    # Ensure there are images to process
    if not images:
        raise Exception("No valid frames to create video.")

    # Create a writer object using imageio for video creation
    writer = imageio.get_writer(output_video_path, fps=fps)
    # Loop through images and add them to the video
    for img in images:

        opencv_image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(opencv_image_rgb)

        # Convert the image to a NumPy array before writing to video
        img_array = np.array(img)
        # Append the image frame to the video
        writer.append_data(img_array)

    # Close the writer to finalize the video file
    writer.close()

    print(f"Video saved to {output_video_path}")