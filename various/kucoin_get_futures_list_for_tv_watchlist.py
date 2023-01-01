import requests
import json

url = "https://api-futures.kucoin.com/api/v1/contracts/active"
response = requests.get(url)
data = json.loads(response.text)

coins = [i["symbol"] for i in data["data"]]

element = ""
for coin in coins:
    coin_cleaned = coin[:-1]
    element += "KUCOIN:" + coin_cleaned + ","
    with open("tradingview_list.txt", "w") as f:
        f.writelines(element)
        f.close()

