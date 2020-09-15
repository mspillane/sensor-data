import redis

r = redis.Redis(host='localhost', port=6379, db=1)
message_queue_name = 'message_queue_01'

def read():
    """
    Reads an item from the message queue
    :return:
    """
    item = r.rpop(message_queue_name)
    # print('read=' + str(item))
    return item

def read_messages():
    """
    Reads messages from the message queue. A generator is returned which can be used
    to iterate over the messages.
    :return: A generator of messages
    """
    count = 0
    while count < 3:
        item = r.rpop(message_queue_name)
        # print('read=' + str(item))
        if item:
            # print('yield:' + str(item))
            yield item
        count += 1

def write(item):
    """
    Writes an item to the message queue
    :param item:
    :return:
    """
    print("Write to message queue:" + str(item))
    r.lpush(message_queue_name, item)

if __name__ == '__main__':
    write("first")
    write("second")
    write("third")

