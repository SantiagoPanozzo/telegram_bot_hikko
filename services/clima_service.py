import requests


class ClimaService:
    def __init__(self, api_key: str):
        self.url = 'https://api.openweathermap.org/data/2.5/find?'
        self.api_key = api_key

    def query(self, lat: float, lon: float):
        return requests.get(f'{self.url}&appid={self.api_key}&lat={lat}&lon={lon}')

