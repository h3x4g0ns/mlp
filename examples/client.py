import socketio
import time

sio = socketio.Client()
sio.connect('http://localhost:42069')

@sio.on('response')
def on_response(data):
    message = data.decode()
    print("recieved", message)


while True:
    sio.emit("hello-world", b" ")
    time.sleep(5)

sio.disconnect()

