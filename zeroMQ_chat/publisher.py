"""The prompt part of a simply two process chat app."""

#
#    Copyright (c) 2010 Andrew Gwozdziewycz
#
#    This file is part of pyzmq.
#
#    pyzmq is free software; you can redistribute it and/or modify it under
#    the terms of the Lesser GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    pyzmq is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    Lesser GNU General Public License for more details.
#
#    You should have received a copy of the Lesser GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import pandas as pd
import zmq
import random
import time
import json

addr = 'tcp://*:49200'

df = pd.read_csv('/home/drogon/Desktop/8th/FYP/iris.csv')
ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)
socket.bind(addr)
#df=list(df)
while True:
    tpl= df.iloc[random.randint(0,len(df)-1),:]
    tpl = tpl.to_json(lines=True, orient='records')

#df = json.dumps(df)

    while True:
        print "sending data"
        socket.send_json((tpl, 'message from server: '))
        time.sleep(0.2)

# try:
#     raw_input          # Python 2
# except NameError:
#     raw_input = input  # Python 3

# def main(addr, who):
#
#     ctx = zmq.Context()
#     socket = ctx.socket(zmq.PUB)
#     socket.bind(addr)
#
#     while True:
#         msg = raw_input("%s> " % who)
#         socket.send_pyobj((msg, who))


# if __name__ == '__main__':
#     import sys
#     if len(sys.argv) != 3:
#         print("usage: publisher.py <address> <username>")
#         raise SystemExit
# main(sys.argv[1], sys.argv[2])