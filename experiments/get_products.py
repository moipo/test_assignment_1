#xml link that works:
# http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=20330&format=xml



import requests
import xmltodict
import json
from pprint import pprint

#link = "http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=20330&format=xml"
link = "http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=22196&format=xml"
response = requests.get(link)
with open('products.xml', 'wb') as file:
    file.write(response.content)


with open('products.xml', "r") as f:
    data = f.read()


d = xmltodict.parse(data)
with open("products.json", 'w') as f:
    f.write(json.dumps(d, indent=4))

products = d["yml_catalog"]["shop"]["offers"]["offer"]
for product in products:
    product["name"]
    product["model"]
    product["price"]
    try:
        product["picture"][0]
    except: pass

    product["url"]
    print("\n\n")


"""
    name = models.CharField(max_length=1000, null = True, default = "", blank = True)
    model = models.CharField(max_length=1000, null = True, default = "", blank = True)
    price = models.IntegerField(null = True, blank = True)
    image = models.CharField(max_length=1000, null = True, default = "", blank = True)
    url = models.CharField(max_length=1000, null = True, default = "", blank = True)
    program = models.ForeignKey("Program", blank = True, null = True, on_delete=  models.SET_NULL)

"""
