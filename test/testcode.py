import requests as rq
import re
from bs4 import BeautifulSoup
#html = open('F:\E-Site Web Crawler\ReviewTest.html', 'rb')
html = open('F:\E-Site Web Crawler\AntiSpider.html', 'rb')
content = BeautifulSoup(html)
#print(content)
pattern = re.compile(r'[a-zA-z]+://[^\s]*')
url = pattern.findall(str(content)) #找到第一个域名
pattern2 = re.compile(r'(?i)^https?://(?:\w+\.)*?(\w*\.(?:com\.cn|cn|com|net))[\\\/]*') #匹配顶级域名
check =  pattern2.findall(url[0])
print(url)
print(check)