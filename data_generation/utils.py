
import random
from datetime import datetime

def random_measurement_time(lower, upper):
    """
    Generates a random measurement time
    :param lower: datetime lower bound
    :param upper: datetime upper bound
    :return: A random time between the lower and upper bounds specified
    """
    # TODO May want to assert that the parameters passed are of type datetime
    random_time = random.randrange(int(lower.timestamp()), int(upper.timestamp()))
    random_time = datetime.fromtimestamp(random_time)
    # print('random_time=' + str(random_time))
    return random_time
