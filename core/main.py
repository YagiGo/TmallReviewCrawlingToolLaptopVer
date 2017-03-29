#! /usr/bin/env python
# -*- coding utf-8 -*-
from core.searchProducts import searchProducts
from core.getReview import getReview
import multiprocessing
from core.getHTML import getPageHtml
import time

'''
def getAllReviews(pageNumber, productNumber, reviewsNumber):
    for i in range(pageNumber):
        htmlFile = open('C:\workspace\TmallReviewCrawlingToolLaptopVer\HTMLSource\第{}页网页代码.html'.format(i+1), 'rb')
        productAndSellerID = searchProducts(htmlFile, i, productName)
        print('第{}页网页源码爬取已完成，准备进行商品信息分析。。。'.format(i + 1))
        reviewsNumberPerPage = getReview(productAndSellerID, productName, reviewPageNumber)
        print('第{}页网页商品评论获取已完成！'.format(i+1))
        htmlFile.close()
        productNumber += len(productName)
        reviewsNumber += reviewsNumberPerPage
'''
        #print(reviewsNumber)
def getAllReviews(pageNumber):
    htmlFile = open('C:\workspace\TmallReviewCrawlingToolLaptopVer\HTMLSource\第{}页网页代码.html'.format(pageNumber + 1), 'rb')
    productAndSellerID = searchProducts(htmlFile, i, productName)
    print('第{}页网页源码爬取已完成，准备进行商品信息分析。。。'.format(i + 1))
    for item in range(len(productAndSellerID)):
        reviewsNumberPerPage = getReview(item, productAndSellerID, productName, reviewPageNumber)
    print('第{}页网页商品评论获取已完成！'.format(i + 1))
    htmlFile.close()
    #productNumber += len(productName)
    #reviewsNumber += reviewsNumberPerPage
    # print(reviewsNumber)

if __name__ == '__main__':
    start = time.clock()
    productName = []
    productNumber = 0
    reviewsNumber = 0
    username = str(input("输入您的天猫账号用户名："))
    password = str(input("输入您的天猫账户密码："))
    keyword = str(input("输入搜索商品的关键字："))
    pageNumber = int(input("请输入想要搜索的页数："))
    reviewPageNumber = int(input("请输入想要爬取得评论的页数："))
    #getPageHtml(username, password, keyword, pageNumber)
    #getAllReviews(pageNumber, productNumber, reviewsNumber)
    for i in range(pageNumber):
        pool = multiprocessing.Pool(processes=8)
        #getAllReviews(i)
        htmlFile = open('C:\workspace\TmallReviewCrawlingToolLaptopVer\HTMLSource\第{}页网页代码.html'.format(pageNumber),
                        'rb')
        productAndSellerID = searchProducts(htmlFile, i, productName)
        productNumber += len(productAndSellerID)
        print('第{}页网页源码爬取已完成，准备进行商品信息分析。。。'.format(i + 1))
        for item in range(len(productAndSellerID)):
            pool.apply_async(getReview, (item, productAndSellerID, productName, reviewPageNumber))
            #reviewsNumberPerPage = getReview(item, productAndSellerID, productName, reviewPageNumber)
        pool.close()
        pool.join()
        print('第{}页网页商品评论获取已完成！'.format(i + 1))
        htmlFile.close()

        '''
        htmlFile = open('C:\workspace\TmallReviewCrawlingToolLaptopVer\HTMLSource\第{}页网页代码.html'.format(i+1), 'rb')
        productAndSellerID = searchProducts(htmlFile, i, productName)
        print('第{}页网页源码爬取已完成，准备进行商品信息分析。。。'.format(i + 1))
        end = len(productAndSellerID)
        reviewsNumberPerPage = getReview(productAndSellerID, productName, reviewPageNumber)
        print('第{}页网页商品评论获取已完成！'.format(i+1))
        htmlFile.close()
        productNumber += len(productName)
        reviewsNumber += reviewsNumberPerPage
        '''
        #print(reviewsNumber)
    end = time.clock()
    print("抓取完毕，一共抓取了{}个商品信息，"
         "耗时{} min".format(productNumber, ((end - start) / 60)))
    # searchProducts(cookies,url)
