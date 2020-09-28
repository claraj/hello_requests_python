import requests


def main():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=minneapolis,us&units=imperal&appid=123456789'  # Replace this with your own URL and key
    data = requests.get(url).json()
    weather_description = data['weather'][0]['description']

    temp_f = data['main']['temp']
    print(f'The weather is {weather_description}, the temperature is {temp_f:.2f}F.')


if __name__ == '__main__':
    main()




