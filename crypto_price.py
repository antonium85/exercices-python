#Description: Get the current price of Bitcoin
#Import the requests library
#Import libraries
import json
import requests
import time
  
# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

while True:
    # requesting data from url
    data = requests.get(key)  
    data = data.json()
    
    #print(data['data']['price'])
    print(f"price is {data['price']}")

    time.sleep(10.0)