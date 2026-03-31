from urllib import response

import requests

API_KEY = "DAZR72VR6C6AVTHW"

API_URL = "https://www.alphavantage.co/"

symbol = "IBM"

def get_stock_market_data():

    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

    print(API_URL+query)

    response = requests.get(url=API_URL+query)

    print(response.json())

   
get_stock_market_data()