# http://old.peihua.cn/stuyqcj/index.aspx?name=34B3180223
import base64
import hashlib
import hmac
import json
import time
import urllib

import requests
import requests as rq
from bs4 import BeautifulSoup

push_config = {
    'HITOKOTO': False,  # 启用一言（随机句子）

    'BARK_PUSH': '',  # bark IP 或设备码，例：https://api.day.app/DxHcxxxxxRxxxxxxcm/
    'BARK_ARCHIVE': '',  # bark 推送是否存档
    'BARK_GROUP': '',  # bark 推送分组
    'BARK_SOUND': '',  # bark 推送声音
    'BARK_ICON': '',  # bark 推送图标

    'CONSOLE': True,  # 控制台输出

    'DD_BOT_SECRET': '',  # 钉钉机器人的 DD_BOT_SECRET
    'DD_BOT_TOKEN': '',  # 钉钉机器人的 DD_BOT_TOKEN

    'FSKEY': '',  # 飞书机器人的 FSKEY

    'GOBOT_URL': '',  # go-cqhttp
    # 推送到个人QQ：http://127.0.0.1/send_private_msg
    # 群：http://127.0.0.1/send_group_msg
    'GOBOT_QQ': '',  # go-cqhttp 的推送群或用户
    # GOBOT_URL 设置 /send_private_msg 时填入 user_id=个人QQ
    #               /send_group_msg   时填入 group_id=QQ群
    'GOBOT_TOKEN': '',  # go-cqhttp 的 access_token

    'GOTIFY_URL': '',  # gotify地址,如https://push.example.de:8080
    'GOTIFY_TOKEN': '',  # gotify的消息应用token
    'GOTIFY_PRIORITY': 0,  # 推送消息优先级,默认为0

    'IGOT_PUSH_KEY': '',  # iGot 聚合推送的 IGOT_PUSH_KEY

    'PUSH_KEY': '',  # server 酱的 PUSH_KEY，兼容旧版与 Turbo 版

    'DEER_KEY': '',  # PushDeer 的 PUSHDEER_KEY

    'PUSH_PLUS_TOKEN': '',  # push+ 微信推送的用户令牌
    'PUSH_PLUS_USER': '',  # push+ 微信推送的群组编码

    'QMSG_KEY': '',  # qmsg 酱的 QMSG_KEY
    'QMSG_TYPE': '',  # qmsg 酱的 QMSG_TYPE

    'QYWX_AM': '',  # 企业微信应用

    'QYWX_KEY': '',  # 企业微信机器人

    'TG_BOT_TOKEN': '',  # tg 机器人的 TG_BOT_TOKEN，例：1407203283:AAG9rt-6RDaaX0HBLZQq0laNOh898iFYaRQ
    'TG_USER_ID': '',  # tg 机器人的 TG_USER_ID，例：1434078534
    'TG_API_HOST': '',  # tg 代理 api
    'TG_PROXY_AUTH': '',  # tg 代理认证参数
    'TG_PROXY_HOST': '',  # tg 机器人的 TG_PROXY_HOST
    'TG_PROXY_PORT': '',  # tg 机器人的 TG_PROXY_PORT
}


def dingding_bot(title: str, content: str) -> None:
    """
    使用 钉钉机器人 推送消息。
    """
    if not push_config.get("DD_BOT_SECRET") or not push_config.get("DD_BOT_TOKEN"):
        print("钉钉机器人 服务的 DD_BOT_SECRET 或者 DD_BOT_TOKEN 未设置!!\n取消推送")
        return
    print("钉钉机器人 服务启动")

    timestamp = str(round(time.time() * 1000))
    secret_enc = push_config.get("DD_BOT_SECRET").encode("utf-8")
    string_to_sign = "{}\n{}".format(timestamp, push_config.get("DD_BOT_SECRET"))
    string_to_sign_enc = string_to_sign.encode("utf-8")
    hmac_code = hmac.new(
        secret_enc, string_to_sign_enc, digestmod=hashlib.sha256
    ).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    url = f'https://oapi.dingtalk.com/robot/send?access_token={push_config.get("DD_BOT_TOKEN")}&timestamp={timestamp}&sign={sign}'
    headers = {"Content-Type": "application/json;charset=utf-8"}
    data = {"msgtype": "text", "text": {"content": f"{title}\n\n{content}"}}
    response = requests.post(
        url=url, data=json.dumps(data), headers=headers, timeout=15
    ).json()

    if not response["errcode"]:
        print("钉钉机器人 推送成功！")
    else:
        print("钉钉机器人 推送失败！")


def postHealthReport(name):
    url = 'http://old.peihua.cn/stuyqcj/index.aspx?name=' + name  # 需要请求的URL地址

    data = {'__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': '/wEPDwUKMTg1OTg4OTU1MWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFhgFAkExBQJBMQUCQTIFAkEyBQJCMQUCQjEFAkIyBQJCMgUCQzEFAkMxBQJDMgUCQzIFAkMzBQJDMwUCRDEFAkQxBQJEMgUCRDIFAkQzBQJEMwUCRjEFAkYyBQJGMwUCRjStGVRunUwdekbVYdAVgrs8LC3YtwjrkxTc7LIeQUNIXQ==',
            '__EVENTVALIDATION': '/wEdABHEPqXkeQtUOWLSv6FkwRhzrVyLxNzBgt1KJuQZ6iZJZHvbOVd7jD77vUTJ9vAbDccHENsdLPywzIncI1Bqene+lBw9tIsm88xZb2QeaC7+SxHn/Prl20L4a14KDWdLx/gcCH+tyiInr+uI0qrtile//yEQBL0aeQ0Xwgupe0bzNu6Y/VkGfFQLatZapz3Bx/aq0T24n4iNXw+FJx9jUxf/WEcduLz4I5EZp/siXfMCgNsHIFw5Q9Z526KmqnVjceuhXfVMuvQwwi4LAJ9Q4hxpTprLTaA28j22ztuekqEzEUmzhk4fH7XS71+9QhewoZ1wHZa9rSvdos3LZrPavMF2zfg78Z8BXhXifTCAVkevd53e7xy2nb59y0IZaUjHCYSgIpsPtmG7wQHn03ODG6Bd',
            'ssq': '陕西省西安市长安区',
            '1': 'A2',
            '2': 'B4',
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
    if name + BeautifulSoup(res_second.text, 'html.parser').find("h2").getText() == name + '今日你已上报完成！':
        dingding_bot("健康上报", name + '今日你已上报完成！')
        return 'OK'
    else:
        dingding_bot("健康上报", name + '未完成健康上报！')
        return 'ERROR'


if __name__ == '__main__':
    print(postHealthReport('')) #学号
