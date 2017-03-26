#! /usr/bin/env python
# -*- coding utf-8 -*-
from pymongo import *
import requests as rq
import re
import time
import random
from core.IPProxy import getIPProxies
from selenium import webdriver
import multiprocessing
def loginTriggered(delayMin, delayMax):
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
    #time.sleep(random.randint(delayMin, delayMax))
    browser.find_element_by_id("TPL_password_1").clear()
    browser.find_element_by_id("TPL_password_1").send_keys(password)
    #time.sleep(random.randint(delayMin, delayMax))
    browser.find_element_by_id("J_SubmitStatic").click() #登录
    #time.sleep(1)
def checkIfCAPTCHATriggered(content):
    noContent = []
    # 可能是触发了验证码也可能没有更多评论显示，需要判断一下
    pattern = re.compile(r'[a-zA-z]+://[^\s]*')
    firstUrl = pattern.findall(content)  # 找到第一个域名,如果是正常的应该是tmall.com
    if(len(firstUrl) == 0):
        return noContent
    else:
        print(content)
        pattern2 = re.compile(r'(?i)^https?://(?:\w+\.)*?(\w*\.(?:com\.cn|cn|com|net))[\\\/]*')  # 匹配顶级域名
        isItCAPTCHA = pattern2.findall(firstUrl[0])  # 如果是触发了验证码，此时的域名应该是taobao.com
        return isItCAPTCHA
def searchAndSaveReviews(urls, username, reviewDate, reviewContent, reviewPageNumber,
                runningTimes, productAndSellerID, item):
    #reviewDict = {}
    previousPage = []
    headers = { 'cookies' : 'otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0;'
                            ' isg=Aq6u9TgGek091Y6-nCVCCnxA_wS7p3KpVUsLzNh18LENu0kVdD_CuVT7BZCt; _tb_token_=7bb63be68b55;'
                            ' uc1=cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false;'
                            ' uc3=nk2=qBEcUqiAxm0%3D&id2=UojTUI6iXcxSKg%3D%3D&vt3=F8dARVQ9KjWKs%2BTvOuY%3D'
                            '&lg2=UtASsssmOIJ0bQ%3D%3D; hng=CN%7Czh-cn%7CCNY;'
                            ' uss=AHxBohD%2B7tK9lzmmt2tA%2Fqz7Wk0HRmtmd6RY9dKLY%2FU28BdJANcjQwDppQ%3D%3D;'
                            ' lgc=%5Cu65AF%5Cu666E%5Cu6B27%5Cu7F57; tracknick=%5Cu65AF%5Cu666E%5Cu6B27%5Cu7F57;'
                            ' cookie2=3a305def162421e5a9c8fba0f099fbba; cookie1=BYEHghnOA%2Bm1NZEPJZ7Ey0emmGcQlwDvuf6T9TdhswM%3D;'
                            ' unb=1974776072; skt=1b01ff0e44a00c38; t=e620fc578685c99f346ee67530dd43cc; _l_g_=Ug%3D%3D; '
                            '_nk_=%5Cu65AF%5Cu666E%5Cu6B27%5Cu7F57; cookie17=UojTUI6iXcxSKg%3D%3D; login=true',
                'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                               'Chrome/57.0.2987.110 Safari/537.36' ,
                'Referer' : 'rate.tmall.com'

    }
    for url in urls:
        #time.sleep(random.randint(1,3))
        count = 0 #抗反爬虫尝试次数
        flag1 = False  # 判断是否正确打开网页，是否触发远程主机强行关闭
        proxies = getIPProxies()
        while not flag1:
            try:
                content = rq.get(url, proxies, headers = headers).text
                flag1 = True
            except:
                print("**************************评论爬取发生错误，将在10-20秒后重试。。。**********************************")
                time.sleep(random.randint(10,20))
                #content = rq.get(url, proxies).text
        #content = rq.get(url, proxies, headers=headers).text
        #time.sleep(random.randint(3,5))
        currentPage = re.findall(re.compile('"rateDate":"(.*?)","reply"'), content)
        print('正在搜索第{}页的评论，请稍后。。。'.format(runningTimes))
        #print(previousPage)
        #print(currentPage)
        if (len(currentPage) == 0):
            # 可能是触发了验证码也可能没有更多评论显示，需要判断一下
            delayMin = 2
            delayMax = 4
            '''pattern = re.compile(r'[a-zA-z]+://[^\s]*')
            firstUrl = pattern.findall(content)  # 找到第一个域名,如果是正常的应该是tmall.com
            pattern2 = re.compile(r'(?i)^https?://(?:\w+\.)*?(\w*\.(?:com\.cn|cn|com|net))[\\\/]*')  # 匹配顶级域名
            isItCAPTCHA = pattern2.findall(firstUrl[0])  # 如果是触发了验证码，此时的域名应该是taobao.com'''
            isItCAPTCHA = checkIfCAPTCHATriggered(content)
            flag2 = False
            while (isItCAPTCHA == ['taobao.com'] and count < 5): #延迟几秒重新加载，直至不再触发
                print('***************************************爬取速度过快，验证码输入被触发！第{}次重试'
                      '************************************************'.format(count + 1))
                #print(isItCAPTCHA[0])
                #time.sleep(random.randint(delayMin, delayMax))
                delayMin += 1
                delayMax += 1
                while flag2 == False:
                    try:
                        #loginTriggered(delayMin , delayMax)
                        content = rq.get(url, proxies, headers = headers).text
                        flag2 = True
                        count += 1
                    except:
                        print("*******************************验证码检测发生错误！即将重试。。。***************************")
                        time.sleep(5)
                #print(content)

                isItCAPTCHA = checkIfCAPTCHATriggered(content)
                flag2 = False
                #urlOnHold.append(url)
            currentPage = re.findall(re.compile('"rateDate":"(.*?)","reply"'), content)
        if(count == 5):
            print('超过重试次数上限，此页放弃！')
            continue
        if (len(currentPage) == 0
                or previousPage == currentPage) and runningTimes >= 3:
            print('*****************************************Bottom Reached********************************************')
            print(previousPage)
            print(currentPage)
            break  # 在没有评论的时候跳出
        username.extend(re.findall('"displayUserNick":"(.*?)"', content))
        #previousPage = re.findall(re.compile('"rateDate":"(.*?)","reply"'), content)
        previousPage = currentPage
        reviewDate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'), content))
        reviewContent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'), content))
        runningTimes += 1
        if runningTimes == reviewPageNumber + 1:
            runningTimes = 0
            # for j in range(0, len(reviewContent)):
            # print(reviewContent[j] + '\n')

    file = open("C:\workspace\TmallReviewCrawlingToolLaptopVer\Reviews\{}.csv".format(productAndSellerID[item][0]),
               'w', encoding='utf-8')

    for i in list(range(0, len(username))):
        file.write(','.join((username[i], reviewDate[i], reviewContent[i])) + '\n')
        #dic = {reviewDate[i]:reviewContent[i]}
        #reviewDict.update(dic)
    #client = MongoClient("localhost", 27017)
    #db = client.test_db
    #collection = db.test_collection
    #collection.insert_one(reviewDict)
    file.close()
    numberOfReviews = len(reviewContent)
    return numberOfReviews
def getUrls(reviewPageNumber, productID, sellerID):
    urls = []
    for i in list(range(reviewPageNumber)):
        urls.append(
            'https://rate.tmall.com/list_detail_rate.htm?itemId={}&sellerId={}&currentPage={}'
                .format(productID, sellerID, i))
        # urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=538921269672&spuId=702279218&sellerId=1714128138&order=3&currentPage=%s'
        # %i)
    return urls
def getReview(item,productAndSellerID, productName, reviewPageNumber):
    reviewsNumber = 0
    '''
    urls = []
    for i in list(range(reviewPageNumber)):
        urls.append(
            'https://rate.tmall.com/list_detail_rate.htm?itemId={}&sellerId={}&currentPage={}'
            .format(productAndSellerID[item][0], productAndSellerID[item][3], i))
        # urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=538921269672&spuId=702279218&sellerId=1714128138&order=3&currentPage=%s'
        # %i)
    '''
    urls = getUrls(reviewPageNumber, productAndSellerID[item][0], productAndSellerID[item][3])
    reviewContent = []
    username = []
    reviewDate = []
    runningTimes = 1

    # print(urls)
    searchAndSaveReviews(urls, username, reviewDate, reviewContent, reviewPageNumber,
                runningTimes, productAndSellerID, item)
    #numberOfReviews = searchAndSaveReviews(urls, username, reviewDate, reviewContent, reviewPageNumber,
    #          runningTimes, productAndSellerID, item)
    #reviewsNumber += numberOfReviews
    #item += 1
    # print(reviewsNumber) 测试评论数量是否正确输出
    return reviewsNumber