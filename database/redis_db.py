import redis
import time

r = redis.Redis(host='localhost', port=6379, db=1)
list_name = "sensor_data_01"

def write(data):
    """
    Write the data to the Redis database
    :param data:
    :return:
    """
    print("Writing data to the database:" + data)
    time.sleep(2) # Add a delay to simulate persisting to a slow database.
    r.rpush(list_name, data)


def read():
    """
    Reada data from the Redis database
    :return:
    """
    item = r.rpop(list_name)
    print('read=' + str(item))
    return item

if __name__ == '__main__':
    write("one")
    write("two")
    write("four")
