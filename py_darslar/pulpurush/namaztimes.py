import requests
# print(requests.__doc__)

url = "https://api.pray.zone/v2/times/today.json?city=tashkent"
res = requests.get(url)
print(res)

