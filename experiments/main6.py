
"""
{"access_token": "2rmWwuEk765vjeIuaP3YriuSdQwAfH",
"expires_in": 604800,
"token_type": "bearer",
"scope": "advcampaigns websites public_data advcampaigns_for_website",
 "refresh_token": "OCTei6OdVGBpRQjoohce4DlJw8cUPm",
  "username": "shaa80",
   "first_name": "\u0410\u043d\u0434\u0440\u0435\u0439",
   "last_name": "\u0411\u043e\u043b\u043e\u0442\u043e\u0432",
    "language": "ru", "id": 1816166,
     "group": "webmaster",
     "code": "nztwz8ig83"

"""

import requests
from pprint import pprint
import json
access_token = "SotGfyXnYgCnNvSgpszeAaXRHnjLvN" # 7 days


"""
curl -L -H 'Authorization: Bearer SotGfyXnYgCnNvSgpszeAaXRHnjLvN' -X GET https://api.admitad.com/advcampaigns/website/2090016/?limit=2
"""
link = "https://api.admitad.com/advcampaigns/website/2090016/?limit=20"


result = requests.get(link, headers={'Authorization': 'Bearer SotGfyXnYgCnNvSgpszeAaXRHnjLvN'})
data = result.json()
# pprint(data)
data = data["results"]
for obj in data:
    pprint(obj)
    # for key in obj.keys():
    #     print(key)

#20-th product feed
pr_feed_link = "http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=2868&format=xml"

pr_feed_link = "http://export.admitad.com/webmaster/websites/2090016/" \
               "products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=2868&format=xml"

# pr_feed_link = "http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=2868&format=xml"
# pr_feed_link = "http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=2868&format=xml"

# import requests
# token = " Basic TXQ0NEJCQ01Ld1lENUJFUExpWTlGRmRhdWwyMXhuOkFESFlJaUJvb2RvUUhIWDVsZVZudTAzbklDa0RDUg=="
# headers={'Authorization': 'TOK:<MY_TOKEN>'}
# requests.post()
#
# refresh_token = "OhWij2hL1GRuKpVUqIzza9eeWJyrVm" #обновляет старый токен