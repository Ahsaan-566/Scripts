import pandas as pd
import zmq
import random
import time

addr = 'tcp://*:6663'

df = pd.read_csv('/home/drogon/PycharmProjects/Data/air.csv')
df2 = pd.read_csv('/home/drogon/PycharmProjects/Data/air2.csv')
ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)
socket.bind(addr)

y = len(df.index)
z = len(df2.index)

# first batch
for x in range(0, y):
    print("sending data")
    socket.send_pyobj((df.iloc[x, :]))
    time.sleep(1)

# second batch
for t in range(0, z):
    print("sending data")
    socket.send_pyobj((df2.iloc[t, :]))
    time.sleep(1)

