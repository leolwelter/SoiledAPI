# Soiled API
The Soiled API is a RESTful service offering capabilities to help users keep
track of plant health and care for them better.

Utilizes Django, and the powerful [DRF](https://www.django-rest-framework.org/).

The API exposes routes for three resources:
- Plant
  - Track watering schedule
  - Has a Sensor
  - Has many Readings, possibly from different Sensors
- Sensor
  - Track status and location
  - Has a Plant
  - Has many Readings
- Reading
  - Many-to-one relation with a Sensor
  - Many-to-one relation with a Plant
  - Each reading holds a timestamp, humidity, and temperature data
    - Humidity readings are relative per individual sensor
    - Temperature readings are in degrees C, and have ±0.5 accuracy.
  
## Installation

### Virtual Environment
1. Navigate to the project root
2. Make sure Python > 3.5 is installed on your system
    - Also install [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
2. Create your virtual environment: `python3 -m venv env`
3. Follow the steps listed [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment)
to activate your virtual environment.
4. Install required packages: `pip3 install -r requirements.txt`

### Setup Django database (sqlite3)
1. Navigate to the project root
2. Run `python manage.py migrate`. This will set up the structure of the database.

### Test Data (optional)
1. Navigate to the project root
2. run `python manage.py loaddata starter_data` to preload a few examples

After making database changes, to create your own starter data, use:
```
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > dump.json
```
To dump only the model data to `dump.json`

## Running
Now that the project is set up, running it is easy.
1. Navigate to the project root
2. Activate your virtualenv
3. Run `python manage.py runserver 8000`

## Tests
Run unit tests by first navigating to the project root, then run:

`python manage.py test`

