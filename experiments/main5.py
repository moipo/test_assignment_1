import requests

access_token = "Bearer SotGfyXnYgCnNvSgpszeAaXRHnjLvN"  # 7 days
link = "https://api.admitad.com/advcampaigns/website/2090016/?limit=5"
result = requests.get(link, headers={'Authorization': 'Bearer SotGfyXnYgCnNvSgpszeAaXRHnjLvN'})
data = result.json()
programs = data["results"]

for program in programs:
    for category in program["categories"]:
        print(category["name"], end=" ")

    print(program["name"])
    print(program["actions_detail"][0]["name"])
    print(program["image"])
    print(program["gotolink"])
    print(program["products_xml_link"])