import pandas as pd
import urllib.request
from lxml import etree
import urllib.error

lj = urllib.request.Request(url='https://www.jieqinwang.com/baike/74283.html',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})

html = urllib.request.urlopen(lj)
html1 = html.read().decode("utf-8")
# h5 = etree.HTML(html1)
# h_1 = h5.xpath("//div[@class='content-left']/article/h1/text()")
# print(h_1)
# try:
#     html = urllib.request.urlopen('https://www.jieqinwang.com/baike/74283.html')
# except urllib.error.HTTPError as e:
#     print("状态码:",e.code)
#     print("原因:",e.reason)
#     print("请求头:",e.headers)
