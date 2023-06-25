from lxml import etree
import urllib.request
import pandas as pd

html = urllib.request.urlopen("https://baijiahao.baidu.com/s?id=1705248934333181423&wfr=spider&for=pc")
view = html.read().decode("utf-8")
with open("就业.html",'w')as j:
    h5 = j.write(str(view))
    j.close()
h5 = etree.HTML(view)
# div[@class='_3mmhnuAOpWJ2lO95fRgCKX']/div[@class='_2xiZo1dd2Za0bMpJ-pdB7B']/div[@class='_1vFr3RWSK0wz54V5vbzAW2']/div[@class='_2OVtLCRVVVa5RwDyfhipoy']/
p1 = h5.xpath("//div[@class='_3mmhnuAOpWJ2lO95fRgCKX']/div[@class='_2xiZo1dd2Za0bMpJ-pdB7B']/div[@class='_1vFr3RWSK0wz54V5vbzAW2']/div[@class='_2OVtLCRVVVa5RwDyfhipoy']/div[@class='_1T4GB1ESohOqTGNmwCAcuf']/h3/span/text()")
# p2 = h5.xpath("//div[@class='main clearfix']/div[@class='mainLeft fl']/div[@class='new_top']/div[@class='new_con']/p/text()")

print(p1)

