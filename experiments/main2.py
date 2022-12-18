import urllib3
from bs4 import BeautifulSoup
import xmltodict
import requests

# ans = requests.post("http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=2868&format=xml")
# print(ans)

http = urllib3.PoolManager()

pr_feed_link = "http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=2868&format=xml"
file = http.request("GET",'https://www.goodreads.com/review/list/20990068.xml?key=nGvCqaQ6tn9w4HNpW8kquw&v=2&shelf=toread')
print(file.data)
# data = file.read()
# file.close()
# data = xmltodict.parse(data)
# print(data)