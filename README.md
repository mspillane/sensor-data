# Sensor Data 
Data engineering project which includes the following 
 * Data generator which simulates data from a set of sensors
 * Module which ingests this data onto a message queue
 * Module which processes message from the queue in parallel using a set of workers which persist the data into a database.

```sh
$ cd sensor-data
$  . ./venv/bin/activate
$ (venv) ~/PycharmProjects/SensorData$ python3 ./pipeline.py
Write to message queue:{"id": "111111", "type": "Sensor", "content": {"temperature_f": -134, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -92}}
Write to message queue:{"id": "111111", "type": "Sensor", "content": {"temperature_f": -218, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -138}}
Write to message queue:{"id": "111111", "type": "Sensor", "content": {"temperature_f": 198, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": 92}}
Write to message queue:{"id": "111111", "type": "Sensor", "content": {"temperature_f": -114, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -81}}
Write to message queue:{"id": "111111", "type": "Sensor", "content": {"temperature_f": -33, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -36}}
Write to message queue:{"id": "111111", "type": "Sensor", "content": {"temperature_f": -337, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -205}}
Write to message queue:{"id": "111111", "type": "Sensor", "content": {"temperature_f": -32, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -35}}
$ 
```

```sh
$ (venv) ~/PycharmProjects/SensorData$ python3 ./process_queue_data.py 
Writing data to the database:b'{"id": "111111", "type": "Sensor", "content": {"temperature_f": -134, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -92}}'
Writing data to the database:b'{"id": "111111", "type": "Sensor", "content": {"temperature_f": -218, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -138}}'
Writing data to the database:b'{"id": "111111", "type": "Sensor", "content": {"temperature_f": 198, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": 92}}'
Writing data to the database:b'{"id": "111111", "type": "Sensor", "content": {"temperature_f": -33, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -36}}'
Writing data to the database:b'{"id": "111111", "type": "Sensor", "content": {"temperature_f": -337, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -205}}'
Writing data to the database:b'{"id": "111111", "type": "Sensor", "content": {"temperature_f": -114, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -81}}'
Writing data to the database:b'{"id": "111111", "type": "Sensor", "content": {"temperature_f": -32, "time_of_measurement": "2020-09-15T11:23:49", "temperature_c": -35}}'
$ 
```
### TODO
  * Add proper logging module
  * Refactor the multiprocessing and simplify functions 
  * Add more unit tests 
  * Convert unit tests to use pytest + tox rather than unittest because this will faciliate using parameterized tests.
  * Redo lint + pep8 on code
  * Provide a requirements.txt file so that this project can be installed using  "pip install -r requirements.txt"
