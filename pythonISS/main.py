import requests
import datetime as dt
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv()

looking = True
sender_email = os.environ.get('sender_email') 
password = os.environ.get('password')
to_email = os.environ.get('to_email')

MY_LAT = 43.546240
MY_LONG = -80.266390

iss_long = 0
iss_lat = 0


def close():
    global iss_long, iss_lat
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_long = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    if MY_LAT - 5 >= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True
    else:
        return False


def night():
    current_hour = dt.datetime.now().hour
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0]) - 5
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0]) - 5
    if current_hour <= sunrise or current_hour >= sunset:
        return True
    else:
        return False


while looking:
    if close() and night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=to_email,
                msg=(f"Subject: ISS Location\n\n"
                     f"Look Up! The ISS is above you now at {iss_long}, {iss_lat}."))
    else:
        pass
    print(iss_long, iss_lat)
    time.sleep(60)
