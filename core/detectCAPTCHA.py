#! /usr/bin/env python
# -*- coding utf-8 -*-
#加入异常处理机制，在验证码输入错误的时候要求重新输入
def detectCAPTCHA(browser):
    if browser.find_elements_by_id('checkcodeInput'):
        captcha = str(input('请输入验证码：'))
        browser.find_element_by_id('checkcodeInput').send_keys(captcha)
        browser.find_element_by_xpath('//input[@type="submit" and @value="确定"]').click()