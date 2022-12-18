import requests
from pprint import pprint

access_token = "SotGfyXnYgCnNvSgpszeAaXRHnjLvN" # 7 days
link = "https://api.admitad.com/advcampaigns/website/2090016/?limit=2"
result = requests.get(link, headers={'Authorization': 'Bearer SotGfyXnYgCnNvSgpszeAaXRHnjLvN'})
data = result.json()

data = data["results"]
for obj in data:
    pprint(obj)

