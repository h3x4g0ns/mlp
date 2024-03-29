import cv2
import base64
import socketio
import numpy as np
import time

# wait 5 seconds for the server to start
print("Waiting 5 seconds for the server to start...")
time.sleep(5)
sio = socketio.Client()
sio.connect("http://localhost:42069")

processed_frame = None

# TODO: Define websocket functions here

while True:
    # TODO: main loop happens here

    pass
