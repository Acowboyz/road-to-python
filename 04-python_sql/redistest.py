from redis import *

r = StrictRedis(host='localhost', port=6379)

# write
# pipe = r.pipeline()
# pipe.set('py1', 'felix')
# pipe.set('py2','world')
# pipe.execute()

# read
# temp = r.get('py1')
# temp2 = r.get('py2')

# print(temp, temp2)

class redisHelper():
    def __init__(self, host, port):
        self.__redis = StrictRedis(host, port)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        return self.__redis.get(key)
