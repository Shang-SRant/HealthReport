import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

url = "http://old.peihua.cn/stuyqcj/index.aspx?name=4988894"
html = requests.get(url).content
bsObj = BeautifulSoup(html, 'html.parser')

VIEWSTATE = bsObj.find('input', {'id': '__VIEWSTATE'}).attrs['value']
EVENTVALIDATION = bsObj.find('input', {'id': '__EVENTVALIDATION'}).attrs['value']

# 输出获取的状态识别码
# print(quote(VIEWSTATE).replace("/", "%2F"))
# print(quote(EVENTVALIDATION).replace("/", "%2F"))

VIEWSTATE = quote(VIEWSTATE).replace("/", "%2F")
EVENTVALIDATION = quote(EVENTVALIDATION).replace("/", "%2F")

name = '51949'
ssq = quote("陕西省西安市长安区")
tiwen = 36.8

i = 1

while i <= 2:
    result = requests.get(
        "http://old.peihua.cn/stuyqcj/index.aspx?name=" + name + "&__EVENTTARGET=&__EVENTARGUMENT&__VIEWSTATE=" +
        VIEWSTATE + "&__EVENTVALIDATION=" +
        EVENTVALIDATION + "&ssq=" + ssq + "&tiwen="+str(tiwen)+"&1=A2&2=B5&3=C2&4=D1&E1=on&E2=on&E3=on&E4=on&lynr1=%E6%97%A0&Button1=%E6%8F%90++++%E4%BA%A4")
    i = i + 1


resultObj = BeautifulSoup(result.content, 'html.parser')

print(resultObj.find("h2").getText())