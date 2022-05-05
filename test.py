# http://old.peihua.cn/stuyqcj/index.aspx?name=34B3180223

import requests as rq
from bs4 import BeautifulSoup

def postHealthReport(name):
    url = 'http://old.peihua.cn/stuyqcj/index.aspx?name=' + name  # 需要请求的URL地址

    data = {'__EVENTTARGET': '',
             '__EVENTARGUMENT': '',
             '__VIEWSTATE': '/wEPDwUKMTg1OTg4OTU1MWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFhgFAkExBQJBMQUCQTIFAkEyBQJCMQUCQjEFAkIyBQJCMgUCQzEFAkMxBQJDMgUCQzIFAkMzBQJDMwUCRDEFAkQxBQJEMgUCRDIFAkQzBQJEMwUCRjEFAkYyBQJGMwUCRjStGVRunUwdekbVYdAVgrs8LC3YtwjrkxTc7LIeQUNIXQ==',
             '__EVENTVALIDATION': '/wEdABHEPqXkeQtUOWLSv6FkwRhzrVyLxNzBgt1KJuQZ6iZJZHvbOVd7jD77vUTJ9vAbDccHENsdLPywzIncI1Bqene+lBw9tIsm88xZb2QeaC7+SxHn/Prl20L4a14KDWdLx/gcCH+tyiInr+uI0qrtile//yEQBL0aeQ0Xwgupe0bzNu6Y/VkGfFQLatZapz3Bx/aq0T24n4iNXw+FJx9jUxf/WEcduLz4I5EZp/siXfMCgNsHIFw5Q9Z526KmqnVjceuhXfVMuvQwwi4LAJ9Q4hxpTprLTaA28j22ztuekqEzEUmzhk4fH7XS71+9QhewoZ1wHZa9rSvdos3LZrPavMF2zfg78Z8BXhXifTCAVkevd53e7xy2nb59y0IZaUjHCYSgIpsPtmG7wQHn03ODG6Bd',
             'ssq': '陕西省西安市长安区',
             '1': 'A1',
             '2': 'B2',
             '3': 'C3',
             '4': 'D3',
             'F1': 'on',
             'F2': 'on',
             'F3': 'on',
             'F4': 'on',
             'Button1': '提    交'
             }  # POST请求需要提交的数据

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    rq.post(url=url, data=data, headers=headers)
    res_second = rq.post(url=url, headers=headers)
    return name + BeautifulSoup(res_second.text, 'html.parser').find("h2").getText()

if __name__ == '__main__':
    print(postHealthReport('34B3180223'))