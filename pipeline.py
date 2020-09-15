import json
from data_generation import data_generator
import message_queue
import transform_data

def run_pipeline():
    for data_point in data_generator.generate():
        # TODO Add proper logging
        data_point_json = json.dumps(data_point)
        # print('data_point=' + data_point_json)
        enriched_data = transform_data.run(data_point_json)
        message_queue.write(str(enriched_data))

if __name__ == '__main__':
    run_pipeline()
