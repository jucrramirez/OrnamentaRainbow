# Third-party libraries
from dotenv import load_dotenv
from pydantic.dataclasses import dataclass
import requests

# Built-in libraries
from datetime import datetime, timedelta, timezone
import os

@dataclass
class WeatherForecasting:
    latitude: float
    longitude: float
    time: datetime

    def __post_init__(self):
        
        _ = load_dotenv()

        # Connection with the TOMORROW forecasting API
        self.secretKey = os.environ.get("OPENWEATHERMAP_KEY")
        self.APIurl = os.environ.get("OPENWEATHERMAP_URL")

    def __post_init_post_parse__(self):

        self.time_UNIX = int(self.time.timestamp())

    def __api_connection__(self):

        querystring = {
            'lat': self.latitude,
            'lon': self.longitude,
            'appid': self.secretKey, 
            'dt': self.time_UNIX,
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
