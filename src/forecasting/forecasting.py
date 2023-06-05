# Third-party libraries
from dotenv import load_dotenv
from pydantic.dataclasses import dataclass
import requests

# Built-in libraries
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
            "location":"33, -84",
            "fields":["temperature", "cloudCover"],
            "units":"metric",
            "timesteps":"5m",
            "apikey":self.secretKey
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
            print("On",date,"it will be", temp, "F")

forecast = WeatherForecasting(1.0, 2.0)
forecast.parsingData()