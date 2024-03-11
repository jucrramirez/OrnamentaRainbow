# Third-party libraries
from dotenv import load_dotenv

# Built-in libraries
from datetime import datetime, timedelta, timezone
import os

# Modules
from forecasting.weatherapp import WeatherForecasting
from forecasting.dateformat import format_date, return_datetime

# LOCATION CONSTANTS
_ = load_dotenv()

LONG = os.environ.get("LONGITUDE")
LAT = os.environ.get("LATITUTE")


if __name__ == '__main__':

    delta_time_days = 15

    start_month = datetime.now().month
    start_day = datetime.now().day
    start_hour = 8

    end_month = datetime.now().month
    end_day = datetime.now().day
    end_hour = 18

    start_date = return_datetime(
        month=start_month, 
        day=start_day, 
        hour=start_hour, 
    ) 

    end_date = return_datetime(
        month=end_month, 
        day=end_day, 
        hour=end_hour, 
    )

    forecasting_start = WeatherForecasting(
        latitude=LAT, 
        longitude=LONG, 
        time=start_date
    )
    
    forecasting_data_start = forecasting_start.get_forecasting()

    forecasting_end = WeatherForecasting(
        latitude=LAT, 
        longitude=LONG, 
        time=end_date
    )
    
    forecasting_data_end = forecasting_end.get_forecasting()
    