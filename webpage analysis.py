#! /usr/bin/env python
# -*- coding = utf-8 -*-
import requests as rq
import urllib.request
import re
#测试天猫的搜索功能和直接进入相关产品页面获得ID的功能
print('输入搜索商品的关键字：')
keyword = str(input("Keword:"))
url = 'https://list.tmall.com/search_product.htm?q={}&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100' \
      '&from=mallfp..pc_1_searchbutton'.format(keyword)
print(url)

#设置Header
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}
#opener = urllib.request.build_opener()
#opener.addheaders = [headers]

#req = opener.open(url)
data = None
req = urllib.request.Request(url, data = None, headers = headers)
#response = urllib.request.urlopen(url)
response = rq.get(url)
content = response.text
file = open('page.html','w')
file.write(content)
file.close()
#需要登录！

print(content)
