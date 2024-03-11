# Built-in libraries
from datetime import datetime, timedelta, timezone

def return_datetime(month, day, hour, minute=0, second=0):
    
    year = datetime.now().year

    return datetime(year, month, day, hour, minute, second)

def format_date(current_date, desired_hour, desired_minute):

    desired_hour = 8
    desired_minute = 00

    # Get the current date
    current_date_= current_date.date()

    # Combine the current date with the desired time
    desired_datetime = datetime.combine(
        current_date_, datetime.min.time()
    ).replace(
        hour=desired_hour,
        minute=desired_minute
    )
        
    return desired_datetime