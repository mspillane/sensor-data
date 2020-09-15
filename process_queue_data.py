import multiprocessing as mp
from itertools import chain, islice
import message_queue
from database import redis_db

number_parallel_processes = 3

def chunks(iterable, size=3):
    iterator = iter(iterable)
    for first in iterator:
        yield chain([first], islice(iterator, size - 1))

def persist_data_point(data_point, output):
    data_point = next(data_point)
    if data_point:
        redis_db.write(str(data_point))
    response = 'data_point: {}'.format(data_point)
    output.put(response)

def process_batch(batch):
    output = mp.Queue()
    processes = [mp.Process(target=persist_data_point, args=(data_point, output)) for data_point in batch]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print('Results from batch write:')
    results = [output.get() for p in processes]
    print(results)

def process_data():
    # Read messages from the data collector in a batch of size 'number_parallel_processes'
    batch = list(chunks(message_queue.read_messages(), number_parallel_processes))
    while batch:
        process_batch(batch)
        batch = list(chunks(message_queue.read_messages(), number_parallel_processes))

def process_data_synchronously():
    for data_point in message_queue.read_messages():
        print('data_point=' + str(data_point))
        if data_point:
            redis_db.write(str(data_point))

if __name__ == '__main__':
    process_data()
    # process_data_synchronously()
