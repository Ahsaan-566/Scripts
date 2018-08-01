from __future__ import print_function
import zmq

import redis
import pickle
import string
import random

def main(addrs):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt(zmq.SUBSCRIBE, "")
    for addr in addrs:
        print("Connecting to: ", addr)
        socket.connect(addr)

    r = redis.StrictRedis(host='localhost', port=6379)
    # while True:

    for y in range(0, 200):

        r.flushall()

        for x in range(0, 200):

        # rando = ''.join([random.choice(string.digits) for n in xrange(5)])
            rando = str(x)
            msg = socket.recv_pyobj()
            pickled_object = pickle.dumps(msg)
            r.set(rando, pickled_object)
            print("Setting object")
            print(rando)
            print("%s: %s" % (msg[1], msg[0]))




if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("usage: display.py <address> [,<address>...]")
        raise SystemExit
main(sys.argv[1:])