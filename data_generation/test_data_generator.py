import unittest
from datetime import datetime
from data_generation import data_generator

class MyTestCase(unittest.TestCase):

    def test_generator(self):
        for i in range(10):
            data_point = next(data_generator.generate())
            # print(str(data_point))
            id = data_point['id']
            type = data_point['type']
            temperature_f = data_point['content']['temperature_f']
            time_of_measurement = data_point['content']['time_of_measurement']
            self.validate_id(id)
            self.validate_fahrenheit(temperature_f)
            self.validate_type(type)
            self.validate_measurement_time(time_of_measurement)

    def validate_fahrenheit(self, temperature):
        if (temperature < data_generator.FAHRENHEIT_LOWER_BOUND or temperature > data_generator.FAHRENHEIT_UPPER_BOUND):
            raise ValueError(
                "Temperature value is not valid Fahrenheit temperature. value={}, lower={}, upper={}".format(
                    temperature, data_generator.FAHRENHEIT_LOWER_BOUND, data_generator.FAHRENHEIT_UPPER_BOUND))

    def validate_type(self, type):
        if type not in data_generator.valid_types:
            raise ValueError("Type value is not a valid. value={}, valid_types={}".format(
                type, data_generator.valid_types))

    def validate_id(self, id):
        pass

    def validate_measurement_time(self, time_of_measurement):
        try:
            datetime.strptime(time_of_measurement, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DDThh:mm:ss")

if __name__ == '__main__':
    unittest.main()
