html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.head)
# print(soup.title)
# print(soup.head.text)
# print(soup.body.b)
# a_list = soup.find_all('a')
# for a in a_list:
#     print(a.get('href'))
#     print(a)
# for tag1 in soup.find_all(re.compile("^b")):
#     print(tag1.name)
# for tag2 in soup.find_all(re.compile("t")):
#     print(tag2.name)
# for tag3 in soup.find_all(True):
#     print(tag3.name)
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print(soup.find_all(has_class_but_no_id))