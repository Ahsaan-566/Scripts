import redis
import pickle
import time

r = redis.StrictRedis(host='localhost', port=6379)

keys = r.keys('*')
while(True):
    print("--------------------------------------------------------")
    time.sleep(5)

    for key in keys:
        # r.flushall()
        # time.sleep(5)

        # type = redis.type(key)
        # if type == KV:
        val = pickle.loads(r.get(key))
        print(val)



# while(True):
# for x in range(0, 200):
#
#     rando = str(x)
#
#     unpacked_object = pickle.loads(r.get(rando))
#     print("Getiing object")
#     print(unpacked_object)