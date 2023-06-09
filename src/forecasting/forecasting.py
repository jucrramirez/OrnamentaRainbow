# Third-party libraries
from dotenv import load_dotenv
from pydantic.dataclasses import dataclass
from suncalc import get_position, get_times
import requests

# Built-in libraries
from datetime import datetime
import os


@dataclass
class WeatherForecasting:
    latitude: float
    longitude: float

    def __post_init__(self):
        _ = load_dotenv()

        # Connection with the TOMORROW forecasting API
        self.secretKey = os.environ.get("TOMORROW_KEY")
        self.APIurl = os.environ.get("TOMORROW_URL")

    def apiConnection(self):
        querystring = {
            "location": "48.888759, 8.705553",
            "fields": ["temperature", "cloudCover"],
            "units": "metric",
            "timesteps": "current",
            "startTime": "now",
            "apikey": self.secretKey
        }

        response = requests.request("GET", self.APIurl, params=querystring)

        return response

    def parsingData(self):

        api_result = self.apiConnection()

        print("Weather Forecast")
        print("================")

        results = api_result.json()['data']['timelines'][0]['intervals']
        for daily_result in results:
            date = daily_result['startTime'][0:10]
            temp = round(daily_result['values']['temperature'])
            cloudDensity = round(daily_result['values']['cloudCover'])

            print("On", date, "at", f"{datetime.now().time()}", "it will be", f"{temp}ºC", f"and the cloud cover percentage will be {cloudDensity}%")

    def sunPosition(self, date):

        return get_position(date, self.longitude, self.latitude)
    
forecast = WeatherForecasting(1.0, 2.0)
forecast.parsingData()

sunposition = forecast.sunPosition(datetime.now())
print(sunposition)
