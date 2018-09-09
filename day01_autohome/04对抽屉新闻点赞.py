#1.登陆，获取cookie
#2.标签url

import requests
from bs4 import  BeautifulSoup

r0=requests.get('http://dig.chouti.com/')
r0_cookie_dict = r0.cookies.get_dict()
r1=requests.post(
    'https://dig.chouti.com/login',
    data={
        'phone':'8615131255089',
        'password':'woshiniba',
        'oneMonth':1
    },
    cookies = r0_cookie_dict
)
r1_cookie_dict = r1.cookies.get_dict()
cookie_dict={}
cookie_dict.update(r0_cookie_dict)
cookie_dict.update(r1_cookie_dict)

print(r1.text)