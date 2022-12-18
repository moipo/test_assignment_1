import traceback
import urllib3
import xmltodict

def getxml():
    url = "http://export.admitad.com/webmaster/websites/2090016/products/export_adv_products/?user=shaa80&code=nztwz8ig83&feed_id=2868&format=xml"

    http = urllib3.PoolManager()

    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
        return -1
    return data
print(getxml())