import requests
import urllib3
import json
from urllib import parse,request
# 禁用warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def gettoken():
    data_to = "code=1138Tkml2vmij94Z31ml2e2dPA18TkmF"
    url_to = 'http://xg.nyist.vip/api/passport/auth'
    h3_to = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate,br',
        'Origin': 'xy.nyist.vip',
        'path': 'api/passport/auth',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'referer': 'https://servicewechat.com/wx5d22ba28f10a2e09/80/page-frame.html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'guest': '',
        'token': '',
        'appid': '1',
    }

    r3 = requests.post(url=url_to, data=data_to.encode("utf-8"), headers=h3_to)
    print(r3.text)


# main
if __name__ == '__main__':
    gettoken()