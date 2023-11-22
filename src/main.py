from flask import Flask, render_template
from flask_socketio import SocketIO
import cv2
import numpy as np
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Dummy ML model function
def process_frame(frame):
    # Process the frame with your ML model here
    # For demonstration, let's just convert it to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

@app.route('/')
def index():
    return "<h1>hello there</h1>" 

@socketio.on('frame')
def handle_frame(data):
    # Decode the frame
    pimg = np.frombuffer(data, dtype=np.uint8)
    frame = cv2.imdecode(pimg, 1)

    # Process the frame
    processed_frame = process_frame(frame)

    # Send back the processed frame
    _, buffer = cv2.imencode('.jpg', processed_frame)
    socketio.emit('response', buffer)

if __name__ == '__main__':
    debug = os.environ.get("DEBUG", None)
    socketio.run(app=app, debug=debug, host="0.0.0.0", port=5050)
