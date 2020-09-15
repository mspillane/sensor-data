import unittest
import datetime
from data_generation import utils

class MyTestCase(unittest.TestCase):

    def test_random_measurement_time(self):
        lower = datetime.datetime.now() - datetime.timedelta(days=7)
        upper = datetime.datetime.now()
        random_time = utils.random_measurement_time(lower, upper)
        assert (type(random_time) is datetime.datetime), \
            "random_measurement_time should return a value of type datetime."
        assert (lower < random_time < upper), "random_measurement_time value is not between the lower and upper bounds."


if __name__ == '__main__':
    unittest.main()
