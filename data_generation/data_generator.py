from datetime import datetime
import random

FAHRENHEIT_LOWER_BOUND = -459 # Absolute zero
FAHRENHEIT_UPPER_BOUND = 212  # Boiling point of water

valid_types = ['Sensor']

def generate():
    count = 0
    while count < 7:
        data_point = {
            'id': '111111',
            'type': 'Sensor',
            'content': {
                'temperature_f': random.randrange(FAHRENHEIT_LOWER_BOUND, FAHRENHEIT_UPPER_BOUND),
                'time_of_measurement': datetime.now().isoformat(timespec='seconds')
            }
        }
        yield data_point
        count += 1
