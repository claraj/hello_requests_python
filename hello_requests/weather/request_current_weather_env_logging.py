import requests
import logging
import os

# Configure the logger - what file to write log messages to,
# and what log level messages (and higher) should be written
logging.basicConfig(filename='weather.log', level=logging.INFO)


def main():

    city = input('What city? ')
    country = input('What country is that in? ')

    try:
        data = get_current_conditions(city, country)

        if data:
            current_temp_f = extract_temperature(data)
            output = f'The current temperature in {city.title()}, {country.upper()} is {current_temp_f:.2f}F'
            logging.info('Successful query with result: ' + output)
            print(output)

        else:
            logging.info('Location %s, %s not found' % (city, country))
            print('This location was not found.')

    except Exception:  # TODO handle different types of error
        # As this is the first statement in the except block, a stack trace will be logged too
        logging.exception('Error fetching current weather data for %s, %s' % (city, country))
        # These are errors that a user can't fix. The developer needs to fix it.
        print('Sorry, there was an error fetching data. '
              'Please check your internet connection, and if that\'s ok, report this to the developer.')


def get_current_conditions(city, country):

    """ Query the Open Weather Map API for the current conditions for a city and country.
    Returns the JSON from Open Weather Map if the location is found
    Return None if the location is not found
    Raises an exception if connection error, API key error etc.
    """

    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    key = os.environ.get('WEATHER_KEY')  # Make sure you set this environment variable
    assert key is not None  # raises an error if environment variable is not set

    # Configure query parameters for the API
    location = '%s,%s' % (city, country)
    params = {'q': location, 'units': 'imperial', 'APPID': key}

    # And make request...
    response = requests.get(base_url, params)

    # Status codes of 200 mean the request was received and processed without error
    if response.status_code == 200:
        return response.json()
    # The API returns 404 (Not Found) if the location can't be found. Check for this and return None
    if response.status_code == 404:
        return None

    # Any other errors, raise an exception
    response.raise_for_status()  # Raise an exception if the status code is not 2xx or 3xx


def extract_temperature(data):
    return data['main']['temp']


if __name__ == '__main__':
    main()
