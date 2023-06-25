import urllib.request
from lxml import etree
import lxml
# he = urllib.request.urlopen("http://www.baidu.com")
# html = he.read().decode('UTF-8')
# with open("baidu","w") as f:
#     f.write(str(html))
#     f.close()
# with open("text.html")as t:
#     text=t.read()
# html1 = etree.HTML(text=text)
# ret_list = html1.xpath("//ul/li")
#
# ret_list1 = ret_list[0].xpath("./a/@href")
# print(ret_list1)

# htm1=urllib.request.urlopen("https://www.tiobe.com/tiobe-index/")
# html2 = htm1.read().decode()
# print(html2[0])

html = urllib.request.urlopen("http://www.baidu.com")
h5 = html.read().decode("utf-8")
lr = etree.HTML(text=h5)
bao = lr.xpath("//img")
print(bao)
# html = urllib.request.Request(url="https://movie.douban.com/chart",headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
# response = urllib.request.urlopen(html)
# view = response.read().decode()
# print(view)




































