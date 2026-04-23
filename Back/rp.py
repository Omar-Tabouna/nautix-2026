import zmq
import cv2
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.33.1:5454")  # Pi's IP
socket.setsockopt(zmq.SUBSCRIBE, b"")      # Subscribe to all messages

print("Connected, waiting for stream...")
while True:
    buffer = socket.recv()
    frame = cv2.imdecode(np.frombuffer(buffer, dtype=np.uint8), cv2.IMREAD_COLOR)
    if frame is None:
        continue

    cv2.imshow("Camera Feed", cv2.rotate(frame, cv2.ROTATE_180))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
socket.close()
context.term()