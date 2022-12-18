import requests

response = requests.get("http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=2868&format=xml", headers={"Accept":"application/xml"})
print(response)
print(response.text)