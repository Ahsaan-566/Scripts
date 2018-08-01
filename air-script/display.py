from __future__ import print_function
import zmq
import threading

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'demo'
pnconfig.publish_key = 'demo'
pubnub = PubNub(pnconfig)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")

socket.connect("tcp://localhost:6663")
print("connected")

def loop():
    # print("loooooooooooooooop")
    threading.Timer(1, loop).start()
    msg = socket.recv_pyobj()
    # print(msg)
    ls = msg.tolist()
    num = ls[4]
    print(num)
    # print(ls[4])
    # dt1 = dt.
    # timestamp = int((time.mktime(dt1.timetuple()) + dt1.microsecond/1000000.0)*1000)
    timestamp = ls[1]
    print(timestamp)
    object1 = dict(time=timestamp, y=num)
    pubnub.publish().channel("awesomeChannel").message(object1)


def main():

    loop()


if __name__ == "__main__":
    main()


