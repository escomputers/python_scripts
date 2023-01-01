import requests
import json

url = "https://api.bybit.com/v2/public/symbols"
response = requests.get(url)
data = json.loads(response.text)
coins = [i["name"] for i in data["result"]]

element = ""
for coin in coins:
    element += "BYBIT:" + coin + ","
    with open("tradingview_list.txt", "w") as f:
        f.writelines(element)
        f.close()


