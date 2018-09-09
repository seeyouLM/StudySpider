#爬取汽车之家新闻

import requests
from bs4 import BeautifulSoup
# 需求一：获取新闻标题
# response = requests.get("https://www.autohome.com.cn/news/")
# response.encoding='gbk'
# soup = BeautifulSoup(response.text,'html.parser')
# tag = soup.find(id='auto-channel-lazyload-article')
# h3 = tag.find_all(name='h3')
# print(h3)

# 需求二：获取新闻标题、图片、简介,url

response = requests.get("https://www.autohome.com.cn/news/")
response.encoding='gbk'
soup = BeautifulSoup(response.text,'html.parser')

li_list = soup.find(id='auto-channel-lazyload-article').find_all(name='li')
for li in li_list:
    title = li.find('h3')   #标题
    if not title:   #判断标题不为空
        continue
    summary = li.find('p').text    #简介
    url = li.find('a').get('href')  #URL
    img_url = li.find('img').get('src') #图片
    print(img_url,title.text,url,summary)
    print("=====================================")

# res = requests.get(url)
# file_name = "%s.jpg"%(title)
# with open(file_name,'w') as f:
#      f.write(res.content)

