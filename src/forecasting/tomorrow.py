# Third-party libraries
from dotenv import load_dotenv
from pydantic.dataclasses import dataclass
import pytz 
import requests

# Built-in libraries
from datetime import datetime
import os


@dataclass
class WeatherForecastingTomorrow:
    latitude: float
    longitude: float
    start_time: datetime
    end_time: datetime
    step: str = "1h"

    def __post_init__(self):
        _ = load_dotenv()

        # Connection with the TOMORROW forecasting API
        self.secretKey = os.environ.get("TOMORROW_KEY")
        self.APIurl = os.environ.get("TOMORROW_URL")

    def __post_init_post_parse__(self):

        start_time_UTC = self.start_time.astimezone(pytz.utc)
        end_time_UTC = self.end_time.astimezone(pytz.utc)

        start_time_ISO_unformatted = start_time_UTC.isoformat()
        end_time_ISO_unformatted = end_time_UTC.isoformat()

        self.start_time_ISO = f"{start_time_ISO_unformatted.split('+')[0]}Z"
        self.end_time_ISO = f"{end_time_ISO_unformatted.split('+')[0]}Z"

    def __api_connection__(self):

        querystring = {
            "location": f"{self.latitude}, {self.longitude}",
            "fields": ["temperature", "cloudCover", "humidity"],
            "units": "metric",
            "timesteps": self.step,
            "startTime": self.start_time_ISO,
            "endTime": self.end_time_ISO,
            "apikey": self.secretKey
        }

        response = requests.request("GET", self.APIurl, params=querystring)

        return response

    def get_forecasting(self):

        forecasting_data = self.__api_connection__()

        return forecasting_data.json()
