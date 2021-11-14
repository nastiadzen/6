import requests
import sys
import re
from bs4 import BeautifulSoup
from collections import Counter
from lxml import etree
from lxml import html
from xml.dom.minidom import parseString
a=requests.get('https://news.ycombinator.com/')
t=[]
y=input('Введіть слово, частоту якого хочете знайти ')
u=BeautifulSoup(a.text, 'html.parser')
for w in y:
    f=u.get_text().lower().count(w)
    d={'phrase': w, 'frequency': f}          
    t.append(d)  
    print('Частота слова', w, ':', f)
m=html.fromstring(a.content)
n=m.cssselect('*')
b= [x.tag for x in n]
c=Counter(b)
for e in c:
    print("Частота html-посилання ", '{}: {}'.format(e, c[e]))
def get_a_cnt(url):
    z=requests.get(url)
    l=etree.HTMLParser()
    k=etree.fromstring(z.content, parser=l)
    return int(k.xpath('count(//a)'))
print("Кількість посилань на сторінці ", get_a_cnt('https://news.ycombinator.com/'))
def get_img_cnt(url):
    j=requests.get(url)
    h=etree.HTMLParser()
    f=etree.fromstring(j.content, parser=h)
    return int(f.xpath('count(//img)'))
print("Кількість зображень на сторінці ", get_img_cnt('https://news.ycombinator.com/'))