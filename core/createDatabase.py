#! /usr/bin/env python
# -*- coding utf-8 -*-
from core.searchProducts import searchProducts
def createDatabase(pageNumber):
    for i in range(20):
        file = open('F:\E-Site Web Crawler\HTMLSource\第{}页网页代码.html'.format(i + 1), 'rb')
        searchProducts(file,i+1)