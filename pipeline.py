from data_generation import data_generator
import message_queue

def run_pipeline():
    for data_point in data_generator.generate():
        # TODO Add proper logging
        print('data_point=' + str(data_point))
        message_queue.write(str(data_point))

if __name__ == '__main__':
    run_pipeline()
