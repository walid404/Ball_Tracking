import os
from flask import Flask, request, jsonify, render_template
import cv2
from utils import *

app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

PROCESSED_FOLDER = 'static/processed_videos'
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_video', methods=['POST'])
def predict_video():
    video = request.files.get('video')

    if not video:
        return jsonify({'error': 'No video file provided'}), 400

    try:
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
        video.save(video_path)

        # Process the video and generate the output predicted video
        output_video_path = process_video(video_path)
        processed_video_url = os.path.join('processed_videos', os.path.basename(output_video_path))
        return jsonify({'predicted_video': processed_video_url})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def process_video(video_path):
    # Create a VideoCapture object to open the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise Exception("Error: Could not open video file.")

    fps = cap.get(cv2.CAP_PROP_FPS)
    rate = 4

    frame_interval = int(fps / rate)
    current_frame = 0
    images = []
    x1, y1 = None, None
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        ret, frame = cap.read()
        if not ret:
            break

        img, x1, y1 = detect_ball(x1, y1, frame)
        if img is not None:
            images.append(img)
        current_frame += frame_interval

    cap.release()

    # Create processed video
    output_video_path = os.path.join(PROCESSED_FOLDER, 'processed_video.mp4')
    create_video_pil(images, rate, output_video_path)

    return output_video_path


from flask import send_from_directory

@app.route('/static/processed_videos/<filename>')
def serve_video(filename):
    return send_from_directory(os.path.join(app.config['PROCESSED_FOLDER']), filename)


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(PROCESSED_FOLDER):
        os.makedirs(PROCESSED_FOLDER)

    app.run(debug=True)
