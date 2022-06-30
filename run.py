import requests
import urllib3

# 禁用warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def func():
    data = "pcc=410000%2C410400%2C410482&gps=34.16717%2C112.84437&location=1&status=0&temp=0&contact=0"
    url3 = 'http://xg.nyist.vip/v1/trace/Student/dailyreportadd'
    h3 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate,br',
        'Origin': 'xy.nyist.vip',
        'path': 'v1/trace/Student/dailyreportadd',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'referer': 'https://servicewechat.com/wx5d22ba28f10a2e09/80/page-frame.html',
        'Content-Type': 'application/x-www-form-urlencoded',
        'guest': 'b2w4YlB2NkosMTQ2LGI0LXBFY2pELDE2NTQxNTEyNDAuMDE3NCw3Nko3NXFYcWJkX2ssZjQwZjNhY2QyZDRjOTMxYzIwMWRiOWU1MDNjNDJkODA=',
        'token': 'af76bc18-e297-4c6a-9b4c-2d0fcda3d3e1',
        'appid': '1',
        'Content-length': '60',
    }
    r3 = requests.post(url=url3,data=data.encode("utf-8"),headers=h3)
    print('\nr3状态码：', r3.text)
