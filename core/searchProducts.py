#! /usr/bin/env python
# -*- coding utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

'''def searchProducts(cookies,url,pageNumber):
    headers = {
        'cookie': cookies
        }
    #headers = {'cookie':cookies}
    #req = urllib.request.Request(url,headers = headers)
    #response = urllib.request.urlopen(req)
    #htmlPage = response.read()
    s = requests.session()
    req = s.get(url,headers = headers)
    htmlPage = req.content
    pageFile = open('homepage.html', 'w')
    #pageFile.write(htmlPage)
    pageFile.close()
    print(htmlPage)
'''
#从获得的网页源文件中获取商品的名称和ID用于最终爬取商品评论
def searchProducts(htmlFile,pageNumber, productName):
    file = BeautifulSoup(htmlFile)
    productAndSeller = []
    productInfo = []
    #print(file.find_all('a', attrs={"target":"_blank","data-p":re.compile(r'^[0-9]*[1-9][0-9]*$-11')}))
    #print(file.find_all('a', attrs={"target": "_blank", "data-p": re.compile(r'-11')}))
    #print(file.find_all('a', attrs = {"data-p":re.compile(r"/^[1-9]\d*$/-11")}, target = '_blank'))
    for list in file.find_all('a', attrs={"target": "_blank", "data-p": re.compile(r'-11')}):
        #print(list)
        #rex = r'<a.*? data-p="-11" "(.*?)".*?>.*?</a>'
        rex = '<a.*? data-p="(.+)" href="(.+)".*?>(.*?)</a>'
        pattern = re.compile(rex)
        list = str(list)
        productInfo.append(re.findall(pattern,list))
    productDatabase = open('C:\workspace\TmallReviewCrawlingToolLaptopVer\Product Information\Product Info database_page {}.csv'
                           .format(pageNumber), 'w')
    for i in range(len(productInfo)):

        if((productInfo[i-1][0][0] != productInfo[i][0][0])):
            pattern2 = re.compile(r'\d+')
            productID = pattern2.findall(productInfo[i][0][1])
            productDatabase.write(','.join((productInfo[i][0][0], productID[0],productID[3],productInfo[i][0][2]))
                                  + '\n')
            productAndSeller.append(productID)
            productName.append(productInfo[i][0][2])
            '''print('production ID is {}'.format(productInfo[i][0][0]) + '\n' +
                  'production url is {}'.format(productInfo[i][0][1]) + '\n' +
                  'production name is {}'.format(productInfo[i][0][2]))'''
    return productAndSeller
def createDatabase(pageNumber):
    for i in range(pageNumber):
        file = open('C:\workspace\TmallReviewCrawlingToolLaptopVer\HTMLSource\第{}页网页代码.html'.format(i + 1), 'rb')
        searchProducts(file,i+1)