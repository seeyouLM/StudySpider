
import requests
from bs4 import BeautifulSoup

res = requests.get("https://new.qq.com/ch/world/")
soup = BeautifulSoup(res.text,'html.parser')
tag = soup.find(id='List').find_all(name='li')
for t in tag:
    url = t.find('a').get('href')
    title = t.img.get('alt')
    print(url)
    print(title)
