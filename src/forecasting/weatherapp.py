# Third-party libraries
from dotenv import load_dotenv
from pydantic.dataclasses import dataclass
import requests

# Built-in libraries
from datetime import datetime
import os, time

@dataclass
class WeatherForecasting:
    latitude: float
    longitude: float

    def __post_init__(self):
        
        _ = load_dotenv()

        # Connection with the TOMORROW forecasting API
        self.secretKey = os.environ.get("OPENWEATHERMAP_KEY")
        self.APIurl = os.environ.get("OPENWEATHERMAP_URL")

    def __api_connection__(self):

        querystring = {
            'lat': self.latitude,
            'lon': self.longitude,
            'appid': self.secretKey, 
            'cnt': 16,
            'timezone': 'utc',
            "units": "metric"
        }
            
        response = requests.get(
            self.APIurl,
            params=querystring
        )

        return response
    
    def get_forecasting(self):
        
        forecasting_data = self.__api_connection__()

        return forecasting_data.json()
