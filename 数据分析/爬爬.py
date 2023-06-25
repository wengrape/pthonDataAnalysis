import urllib.request
from lxml import etree

with open("view1.html")as html:
    h5=html.read()
    html.close()


a = etree.HTML(h5)
href = a.xpath("//meta/@name")
print("src:",href)
