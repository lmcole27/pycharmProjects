
import smtplib
import datetime as dt
import time
import os 
from dotenv import load_dotenv

load_dotenv()


with open("quotes.txt", "r") as file:
    quote = file.readlines(0)

sender_email = os.environ.get('SENDER_EMAIL')
password = os.environ.get('PASSWORD')
to_email = os.environ.get('TO_EMAIL')

y = 0
x = True
need_quote = True

while x:
    now = dt.datetime.now()
    today = now.weekday()
    #today = int(now.strftime("%w"))
    #print(type(today), today)
    if today == 5 and need_quote:
        today_quote = (quote[y])
        print(today_quote)
        y += 1
        need_quote = False
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=to_email,
                msg=(f"Subject: Motivational Quote Minute\n\n"
                    f"This Motivational Minute Quote is: {today_quote}"))
    elif today == 0:
        need_quote = True
    else:
        time.sleep(60)
        need_quote = True

        print(f"checking if you need a quote: {need_quote}")




