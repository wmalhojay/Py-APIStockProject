# **** represents YOUR OWN API code, key ...etc

import requests
from datetime import *
from newsapi import NewsApiClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
currentDate = datetime.now().date()
previousDate = currentDate - timedelta(days=1)
dayBeforePreviousDate = currentDate - timedelta(days=2)

Nparams = {
    "q": COMPANY_NAME,
    "from": dayBeforePreviousDate,
    "to": previousDate,
    "apiKey": "****",
}

Tnews = requests.get("https://newsapi.org/v2/everything", params=Nparams)
Tnews.raise_for_status()
latestNews = Tnews.json()['articles'][0]

Tparams = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": "****"
}

Tstock = requests.get("https://www.alphavantage.co/query", params=Tparams)
Tstock.raise_for_status()
Tstock = Tstock.json()["Time Series (Daily)"]

closingPerStockPriceDifference = float(Tstock[f"{previousDate}"]["4. close"]) - float(Tstock[f"{dayBeforePreviousDate}"]["4. close"])
if closingPerStockPriceDifference < 0:
    closingPerStockPriceDifference = abs(closingPerStockPriceDifference)/float(Tstock[f"{previousDate}"]["4. close"]) * 100
    closingPerStockPriceDifference = f"🔻 {round(closingPerStockPriceDifference, 2)}%"
else:
    closingPerStockPriceDifference = closingPerStockPriceDifference/float(Tstock[f"{previousDate}"]["4. close"]) * 100
    closingPerStockPriceDifference = f"🔺 {round(closingPerStockPriceDifference, 2)}%"

print("-----------------------------------\n\n"
      f"STOCK: {STOCK}\n"
      f"COMPANY: {COMPANY_NAME}\n"
      f"DATE: {previousDate}\n"
      f"STOCK PRICE DIFFERENCE: {closingPerStockPriceDifference}\n"
      f"Title: {latestNews['title']}\n"
      f"Description: {latestNews['description']}\n"
      f"From : {latestNews['source']['name']} --uploaded by--> {latestNews['author']} -at-> {latestNews['publishedAt']} \n\n----------------------------------")



