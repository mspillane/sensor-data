import json
import unittest
import transform_data

class MyTestCase(unittest.TestCase):

    def test_transform_data(self):
        data_point = {
            'id': '111111',
            'type': 'Sensor',
            'content': {
                'temperature_f': 212,
                'time_of_measurement': '2019-06-24T15:00:00'
            }
        }
        data_point_json = json.dumps(data_point)
        transformed_data = transform_data.run(data_point_json)
        transformed_data = json.loads(transformed_data)
        temperature_c = transformed_data['content']['temperature_c']
        assert (temperature_c == 100), "Celsius temperature does not match expected."


    def test_fahrenheit_to_celsius(self):
        fahrenheit_to_celsius_map = {
            "32": 0,
            "212": 100
        }
        for fahrenheit, celsius in fahrenheit_to_celsius_map.items():
            print('map: fahrenheit={}, celsius={}' + fahrenheit, celsius)
            celsius_calculated = transform_data.fahrenheit_to_celsius(int(fahrenheit))
            assert (celsius_calculated == celsius), \
                "Celsius calculated does not match expected value. fahreneheit={}, celsius={}, calculated={}"\
                .format(fahrenheit, celsius, celsius_calculated)

if __name__ == '__main__':
    unittest.main()
