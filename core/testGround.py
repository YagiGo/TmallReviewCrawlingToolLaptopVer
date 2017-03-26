#! /usr/bin/env python
# -*- coding utf-8 -*-
#用于对还在开发中的函数和文件进行实验
from core.searchProducts import searchProducts
from selenium import webdriver
import time
'''for i in range(20):
    file = open('F:\E-Site Web Crawler\HTMLSource\第{}页网页代码.html'.format(i + 1), 'rb')
    searchProducts(file,i+1)
'''
'''productName = []
file = open('C:\workspace\TmallReviewCrawlingToolLaptopVer\HTMLSource\第1页网页代码.html', 'rb')
productAndSellerID = searchProducts(file,1,productName)
print(len(productAndSellerID))
print(len(productName))
for item in range(len(productName)):
    print(productName[item])
    print(productAndSellerID[item][0] + ' ' + productAndSellerID[item][3])'''
def loginTriggered():
    browser = webdriver.Chrome()
    url = 'https://sec.taobao.com/query.htm?action=QueryAction&event_submit_do_css=ok&smApp=tmallrateweb&smPolicy=' \
          'tmallrateweb-rate-anti_Spider-checklogin&smCharset=GBK&smTag=MjIzLjcyLjcwLjExMywsZjNlZGRhMjBkNmM4NGE5Mzg4N' \
          'jA0YjJkNzU2NzY4YzI%3D&smReturn=https%3A%2F%2Frate.tmall.com%2Flist_detail_rate.htm%3FitemId%3D535408892361%26' \
          'sellerId%3D849727411%26currentPage%3D50&smSign=V%2Fvid%2F75HKxVw4UkZ10YxA%3D%3D'
    username = '斯普欧罗'
    password = 'wuzh8285xin618'
    browser.get(url)
    browser.find_element_by_id("TPL_username_1").clear()
    browser.find_element_by_id("TPL_username_1").send_keys(username)
    time.sleep(3)
    browser.find_element_by_id("TPL_password_1").clear()
    browser.find_element_by_id("TPL_password_1").send_keys(password)
    time.sleep(3)
    browser.find_element_by_id("J_SubmitStatic").click() #登录
    time.sleep(1)