import requests
from twilio.rest import Client
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.environ.get('ACCOUNT_SID') 
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
client = Client(ACCOUNT_SID, AUTH_TOKEN)

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
UP = "🔺"
DOWN = "🔻"

current_date = str(dt.date.today() - dt.timedelta(days=1))
previous_date = str(dt.date.today() - dt.timedelta(days=2))

## Use https://www.alphavantage.co - Calculate % change in stock price

alpha_url="https://www.alphavantage.co/query?"
alpha_api_key = os.environ.get('alpha_api_key')
alpha_parameters = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": STOCK, "outputsize": "full", "apikey": alpha_api_key}
alpha_request = requests.get(url=alpha_url, params=alpha_parameters)
alpha_data = alpha_request.json()

today = float(alpha_data["Time Series (Daily)"][current_date]["4. close"])
yesterday = float(alpha_data["Time Series (Daily)"][previous_date]["4. close"])

percentage_change = (today - yesterday)/yesterday*100
if percentage_change >= 0:
    symbol = UP
else:
    symbol = DOWN


## STEP 2: Use https://newsapi.org to get the first 3 news pieces for the COMPANY_NAME.

news_api_key = os.environ.get('news_api_key')
news_parameters = {"q": COMPANY_NAME, "from": previous_date, "to": current_date, "language": "en", "sortBy": "relevancy", "apiKey": news_api_key}
#news_url = "https://newsapi.org/v2/everything?q=tesla&from=2023-02-25&sortBy=publishedAt&apiKey=e2fe1af6bb5c4942a9392c2f037ffca0"
news_url="https://newsapi.org/v2/everything"
news_request = requests.get(url=news_url, params=news_parameters)
news_data = news_request.json()
top_news = news_data["articles"][0:3]


for story in range(3):
    content = f"{STOCK} {symbol} {abs(percentage_change):.2f}%\n" \
              f"Headline: {top_news[story]['title']} \n" \
              f"Brief: {top_news[story]['description']}"
    
    print(content)
