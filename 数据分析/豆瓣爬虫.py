import urllib.request
from lxml import etree
# 二手房
html1 = urllib.request.Request(url="https://cs.anjuke.com/sale",headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'})
html = urllib.request.urlopen(html1)
view = html.read().decode("utf-8")

# print(view)

h5 = etree.HTML(view)
zp = h5.xpath("//div[@class='list']/section[@class='list-body']/section[@class='list-main']/section[@class='list-left']/section[@class='list']/div[@class='property']/a/div[@class='property-image']/img/@src")
# zp = h5.xpath("//section[class='list']/div[@class='property']/a/div[@class='property-image']")
print(zp)

# html1 = urllib.request.urlopen("https://cs.anjuke.com/sale")
# view1 = html1.read().decode("utf-8")
#
# # with open("view1.html",'w')as v:
# #     w = v.write(str(view1))
# #     v.close()
# a = etree.HTML(view1)
# href = a.xpath("//div/div/div/section/section/section/section/div/a/div[@class='property-image']/img/@src")
# print("src:",href)
