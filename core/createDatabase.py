#! /usr/bin/env python
# -*- coding utf-8 -*-
from core.searchProducts import searchProducts
def createDatabase(pageNumber):
    for i in range(20):
        file = open('C:\workspace\TmallReviewCrawlingToolLaptopVer\HTMLSource\第{}页网页代码.html'.format(i + 1), 'rb')
        searchProducts(file, i+1)