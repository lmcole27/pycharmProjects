import datetime as dt
import os

from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    API_KEY = os.environ.get('API_KEY')
    ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
    location = "YYZ"
    destination = "YYT"
    parameters = {"fly_from" : "location", "date_from": "", "date_to": ""}

    pass


today = dt.datetime.now()
date = today.date()
date_return = dt.timedelta(7)
print(f"today is {today} date is {date}")
print(f"next week is {date_return}")

