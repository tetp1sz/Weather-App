import requests

class Weather:
    def __init__(self, city):
        self.city = city
        self.temp = 0
        self.weather = self.date = self.detail_weather = ''
        self.key = '144546767c7cb8e1782ee5d0a85b2196'
        self.res = requests.get('https://api.openweathermap.org/data/2.5/forecast', params={
            'q': city,
            'units': 'metric',
            'lang': 'EN',
            'APPID': self.key
        })
        self.data = self.res.json()

    def get_emoji(self):
        emoji = ''
        if self.weather == 'Clear':
            emoji = '☀️'
        elif 'Clouds' in self.weather:
            emoji = '⛅'
        elif self.weather == 'Shower rain':
            emoji = '🌧️'
        elif self.weather == 'Rain':
            emoji = '🌦️'
        elif self.weather == 'Thunderstorm':
            emoji = '🌩️'
        elif self.weather == 'Snow':
            emoji = '🌨️'
        elif self.weather == 'Mist':
            emoji = '🌫️'
        return emoji

    def print_weather(self):
        error = False
        try:
            for i in self.data['list']:
                self.date = i['dt_txt']
                self.temp = '{0:+3.0f}'.format(i['main']['temp'])
                self.weather = i['weather'][0]['main']
                self.detail_weather = i['weather'][0]['description']
            return f'Date: {self.date}\nTemperature: {self.temp} °C\nWeather: {self.weather} {self.get_emoji()}\nWeather details: {self.detail_weather}'
        except Exception:
            return f'>>> City not found'