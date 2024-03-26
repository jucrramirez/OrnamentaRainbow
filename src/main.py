# Third-party libraries
from dotenv import load_dotenv

# Built-in libraries
from datetime import datetime, timedelta, timezone
import json, os

# Modules
from forecasting.weatherapp import WeatherForecasting
from forecasting.tomorrow import WeatherForecastingTomorrow
from forecasting.dateformat import return_datetime
from misc.evaluate import get_probability


# LOCATION CONSTANTS
_ = load_dotenv()

LONG = os.environ.get("LONGITUDE")
LAT = os.environ.get("LATITUTE")


if __name__ == '__main__':

    start_month = datetime.now().month
    start_day = datetime.now().day
    start_hour = 8

    end_month = datetime.now().month
    end_day =  datetime.now().day
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

    # ______________________________________________WeatherForecastingTomorrow________________________________________________
    # Using WeatherForecastingTomorrow you just need to create one istance, and send the start_time and the endtime
    # to the constructor. The only valid values for the "step parameter" are here: https://docs.tomorrow.io/reference/weather-data-layers
    # Please take a look at the limitations of the number of API requests.
    # ________________________________________________________________________________________________________________________


    forecastingTomorrow = WeatherForecastingTomorrow(
        latitude=LAT,
        longitude=LONG, 
        start_time=start_date,
        end_time=end_date,
        step="1h"
    )

    forecasting_data = forecastingTomorrow.get_forecasting()

    for item in forecasting_data["data"]["timelines"]:
        intervals = item["intervals"]
        for interval_data in intervals:
            cloudiness = interval_data["values"]["cloudCover"]
            probability_based_on_cloudiness = get_probability(cloudiness)

            print(f"Cloudiness: {cloudiness} & Probability: {probability_based_on_cloudiness}")


    # ________________________________________WeatherForecasting _____________________________________________________________
    # WeatherForecasting data is limitated, it extracts the data from today midday and for the next 16 days (midday as well).
    # I would recommend you to use the WeatherForecastingTomorrow service instead.
    # ________________________________________________________________________________________________________________________

    forecasting = WeatherForecasting(
        latitude=LAT, 
        longitude=LONG, 
    )

    forecasting_data = forecasting.get_forecasting()


    for item in forecasting_data["list"]:

        cloudiness = float(item["clouds"])

        probability_based_on_cloudiness = get_probability(cloudiness)

        # print(f"Cloudiness: {cloudiness} & Probability: {probability_based_on_cloudiness}")