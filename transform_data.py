import json

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert fahrenheit to celsius
    :param fahrenheit:
    :return:
    """
    celsius = int((fahrenheit - 32) * 5/9)
    # print("fahrenheit={}, celsius={}".format(fahrenheit, celsius))
    return celsius

def add_celsius_temperature(data_item):
    """
    Adds a key-value for the celsius temperature to a data point
    :param data_item: Data point to be updated
    :return: Data point with added celsius temperature
    """
    data_point = json.loads(data_item)
    content = data_point['content']
    content['temperature_c'] = fahrenheit_to_celsius(content['temperature_f'])
    return json.dumps(data_point)

def run(data_item):
    """
    Run the transformation(s) on the data point provided
    :param data_item:
    :return: A data point enriched with additional data
    """
    # print(f'Transforming: {data_item}')
    enriched_data = add_celsius_temperature(data_item)
    return enriched_data
