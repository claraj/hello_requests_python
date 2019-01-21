import requests
import os


def main():

    city = input('What city? ')
    country = input('What country is that in? ')

    try:
        data = get_current_conditions(city, country)

        if data:
            current_temp = extract_temperature(data)
            print(f'The current temperature in {city.title()}, {country.upper()} is {current_temp:.2f}F')

        else:
            print('This location was not found.')

    except Exception as e:  # TODO handle different types of error
        print('Sorry, there was an error fetching data. '
              'Please check your internet connection, and if that\'s ok, report this to the developer.', e)



def get_current_conditions(city, country):

    """ Query the Open Weather Map API for the current conditions for a city and country.
    Returns the JSON from Open Weather Map if the location is found
    Return None if the location is not found
    Raises an exception if connection error, API key error etc.
    """

    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    key = os.environ['WEATHER_KEY']  # Make sure you set this environment variable
    assert key is not None # raises an error if environment variable is not set

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
