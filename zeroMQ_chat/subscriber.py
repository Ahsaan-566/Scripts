from __future__ import print_function
import zmq


def main(addrs):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt(zmq.SUBSCRIBE, "")
    for addr in addrs:
        print("Connecting to: ", addr)
        socket.connect(addr)

    while True:
        msg = socket.recv_json()
        print("%s: %s" % (msg[1], msg[0]))


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("usage: subscriber.py <address> [,<address>...]")
        raise SystemExit
main(sys.argv[1:])