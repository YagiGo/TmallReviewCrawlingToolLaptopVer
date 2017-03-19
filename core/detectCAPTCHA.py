#! /usr/bin/env python
# -*- coding utf-8 -*-
def detectCAPTCHA(browser):
    if (browser.find_elements_by_id('checkcodeInput')) :
        captcha = str(input('请输入验证码：'))
        browser.find_element_by_id('checkcodeInput').send_keys(captcha)
        browser.find_element_by_xpath('//input[@type="submit" and @value="确定"]').click()