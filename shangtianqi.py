import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

url = "http://old.peihua.cn/stuyqcj/index.aspx?name=4988894"
html = requests.get(url).content
bsObj = BeautifulSoup(html, 'html.parser')
# print(bsObj)

VIEWSTATE = bsObj.find('input', {'id': '__VIEWSTATE'}).attrs['value']
EVENTVALIDATION = bsObj.find('input', {'id': '__EVENTVALIDATION'}).attrs['value']

print(quote(VIEWSTATE).replace("/", "%2F"))
print(quote(EVENTVALIDATION).replace("/", "%2F"))

A = quote(VIEWSTATE).replace("/", "%2F")
B = quote(EVENTVALIDATION).replace("/", "%2F")

name = '34B3180223'
ssq = quote("陕西省咸阳市秦都区")

i = 1

while i <= 2:
    result = requests.get(
        "http://old.peihua.cn/stuyqcj/index.aspx?name=" + name + "&__EVENTTARGET=&__EVENTARGUMENT&__VIEWSTATE=" +
        A + "&__EVENTVALIDATION=" +
        B + "&ssq=" + ssq + "&tiwen=36.8&1=A2&2=B5&3=C2&D1=on&D2=on&D3=on&D4=on&lynr1=%E6%97%A0&Button1=%E6%8F%90++++%E4%BA%A4")
    i = i + 1
resultObj = BeautifulSoup(result.content, 'html.parser')
print(resultObj.find("h2").getText())
