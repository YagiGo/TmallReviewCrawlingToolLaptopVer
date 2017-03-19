#! /usr/bin/env python
# -*- coding utf-8 -*-
import random
import time

from selenium import webdriver

from core.detectCAPTCHA import detectCAPTCHA
from core.searchProducts import searchProducts

def getPageHtml(username,password,keyword,pageNumber):
    browser = webdriver.Chrome()
#输入关键字之后首先会要求登录！此函数的目的是获取cookies
#print('输入搜索关键字：')
#keyword = str(input("keyword:"))
#url = 'https://list.tmall.com/search_product.htm?q={}&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100' \
#      '\&from=mallfp..pc_1_searchbutton'.format(keyword)
#url = 'https://list.tmall.com/search_product.htm?q=shouji&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100' \
#      '&from=mallfp..pc_1_searchbutton'
    url = 'https://login.taobao.com/member/login.jhtml?tpl_redirect_url=%2F%2Fwww.tmall.hk&style=miniall&enup=' \
          'true&newMini2=true&full_redirect=true&sub=true&from=tmall&allp=assets_css%3D3.0.6%2Fapps%2Fhk%2Flogin_pc' \
          '.css&pms=1489401306612%22'
    browser.get(url) #open the web page
#login.taobao.com/member/login.jhtml?tpl_redirect_url=%2F%2Fwww.tmall.hk&style=miniall&enup=true&newMini2=true&full_redirect=true&sub=true&from=tmall&allp=assets_css%3D3.0.6%2Fapps%2Fhk%2Flogin_pc.css&pms=1489401306612"
#登录网址
#assert "Tmall" in browser.title
#username
    time.sleep(1)

    browser.find_element_by_id("J_Quick2Static").click() #切换到账户密码输入
    browser.find_element_by_id("TPL_username_1").clear()
    browser.find_element_by_id("TPL_username_1").send_keys(username)
    browser.find_element_by_id("TPL_password_1").clear()
    browser.find_element_by_id("TPL_password_1").send_keys(password)
    browser.find_element_by_id("J_SubmitStatic").click() #登录
    time.sleep(1)
    #browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') #mac系统是command win和linux是ctrl
    browser.get('https://www.tmall.com') #转到天猫首页
    time.sleep(1)
    detectCAPTCHA(browser) #验证码检测
    browser.find_element_by_name('q').clear()
    browser.find_element_by_name('q').send_keys(keyword) #输入搜索的关键字
    detectCAPTCHA(browser) #验证码检测
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    #在被要求输入验证码的时候提醒用户手动输入验证码
    #find_elements在没有找到指定元素时会返回空list，可用于判断
    '''if (browser.find_elements_by_id('checkcodeInput')) :
        captcha = str(input('请输入验证码：'))
        browser.find_element_by_id('checkcodeInput').send_keys(captcha)
        browser.find_element_by_xpath('//input[@type="submit" and @value="确定"]').click()'''
    #上面的代码已重构，放在了detectCAPTCHA.PY
    detectCAPTCHA(browser) #验证码检测
        #find_elements_by_xpath returns list of WebElements.
        # It should be find_element_by_xpath. Note the s in find_element.

    #browser.find_element_by_xpath("//div[@id='filter clearfix'][@title='点击后按人气从高到低'") //销量从高到低排列 TODO

    for i in range(pageNumber):

        html_source = (browser.page_source).encode('utf-8') #得到当前页的html网址 按照utf-8
        file = open('F:\E-Site Web Crawler\HTMLSource\第{}页网页代码.html'.format(i+1), 'wb')
        print('正在获取第{}页的网页html代码，html文件可在htmlSource目录下找到'.format(i + 1))
        file.write(html_source)
        file.close()
        browser.find_element_by_class_name('ui-page-next').click()
        # 在被要求输入验证码的时候提醒用户手动输入验证码
        '''if (browser.find_elements_by_id('checkcodeInput')):
            captcha = str(input('请输入验证码：'))
            browser.find_element_by_id('checkcodeInput').send_keys(captcha)
            browser.find_element_by_xpath('//input[@type="submit" and @value="确定"]').click()'''
        # 上面的代码已重构，放在了detectCAPTCHA.PY
        detectCAPTCHA(browser)  #验证码检测
        time.sleep(random.randint(1,4)) #随机延时3-8秒
    #browser.find_element_by_xpath("//div[@class='fsort' and @title='点击后按月销量从高到低'")
    #time.sleep(20)

#browser.find
#get Cookie 当url变化之后认定登录完成，开始获取cookies
'''    while True:
        if browser.current_url != url:
            break
        time.sleep(1)
    for item in browser.get_cookies():
        cookies = [item["name"] + "=" + item["value"]]
    #print(cookies)
    #browser.quit()

    cookiestr = ';'.join(item for item in cookies)
    #print('\n' + cookiestr)
    return cookiestr
'''
