# http://old.peihua.cn/stuyqcj/index.aspx?name=34B3180223

import requests as rq
from bs4 import BeautifulSoup


def postHealthReport(name, zhenshu):
    url = 'http://old.peihua.cn/stuyqcj/index.aspx?name=' + name  # 需要请求的URL地址

    data = {'__EVENTTARGET': '',
             '__EVENTARGUMENT': '',
             '__VIEWSTATE': '/wEPDwULLTE3ODE2MTI0ODlkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYgBQJBMQUCQTEFAkEyBQJBMgUCQjEFAkIxBQJCMgUCQjIFAkIzBQJCMwUCQjQFAkI0BQJDMQUCQzEFAkMyBQJDMgUCRDEFAkQxBQJEMgUCRDIFAkUxBQJFMQUCRTIFAkUyBQJFMwUCRTMFAkU0BQJFNAUCRjEFAkYyBQJGMwUCRjQloBKkQUjJyEQXV7bz2cZV67XSweGjK+vQdnjG6VaJug==',
             '__EVENTVALIDATION': '/wEdABbqp31eMH/8aK/n2m23NorDrVyLxNzBgt1KJuQZ6iZJZHvbOVd7jD77vUTJ9vAbDccHENsdLPywzIncI1Bqene+lBw9tIsm88xZb2QeaC7+SxHn/Prl20L4a14KDWdLx/iTm9Z5ttIPd2nzuFjHGlpc7H91ulAMzy+qTw/3CR3CMxwIf63KIiev64jSqu2KV7//IRAEvRp5DRfCC6l7RvM2qtE9uJ+IjV8PhScfY1MX/1hHHbi8+CORGaf7Il3zAoCWVJwQeCzMvfvbSKmFiRyBmmdqzL/YNIzFlXqGANynIP4KDOAORxNv6rPYjm8CFB+29oj+CDKDZCNEkBlqP9GkoV31TLr0MMIuCwCfUOIcaU6ay02gNvI9ts7bnpKhMxFJs4ZOHx+10u9fvUIXsKGdcB2Wva0r3aLNy2az2rzBdgSZ4+KsAgqDt1MJc9qdjo/N+DvxnwFeFeJ9MIBWR693rL5j3AQJGEm1JdxrJlVuo6bhz1vC05BxRi8fjoNR6wk=',
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
    print(postHealthReport('34B3190102'))
    print(postHealthReport('34B3180223'))
