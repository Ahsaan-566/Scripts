import zmq
import time
import random
import sys

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:6666")

while True:
    msg = socket.recv()
    print(msg)
    socket.send_string("Received tuple")
