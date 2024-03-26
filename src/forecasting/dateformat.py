# Built-in libraries
from datetime import datetime, timedelta, timezone

def return_datetime(month, day, hour, minute=0, second=0):
    
    year = datetime.now().year

    return datetime(year, month, day, hour, minute, second)
