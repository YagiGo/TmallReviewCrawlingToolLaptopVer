#! /usr/bin/env python
# -*- coding utf-8 -*-
#用于对还在开发中的函数和文件进行实验
from core.searchProducts import searchProducts
'''for i in range(20):
    file = open('F:\E-Site Web Crawler\HTMLSource\第{}页网页代码.html'.format(i + 1), 'rb')
    searchProducts(file,i+1)
'''
productName = []
file = open('F:\E-Site Web Crawler\HTMLSource\第1页网页代码.html', 'rb')
productAndSellerID = searchProducts(file,1,productName)
print(len(productAndSellerID))
print(len(productName))
for item in range(len(productName)):
    print(productName[item])
    print(productAndSellerID[item][0] + ' ' + productAndSellerID[item][3])