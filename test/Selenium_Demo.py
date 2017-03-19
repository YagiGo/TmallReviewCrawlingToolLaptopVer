from selenium import webdriver
import time
username = 'wuzhxin'
password = '123456'
browser = webdriver.Chrome()
url = "https://login.taobao.com/member/login.jhtml"
browser.get(url)
    #转到iframe里面去
'''browser.switch_to_frame(browser.find_element_by_name("taobaoLoginIfr"))
    #输入用户名
browser.find_element_by_id("TPL_username_1").clear()
browser.find_element_by_id("TPL_username_1").send_keys(username)
    #输入密码
browser.find_element_by_id("TPL_password_1").clear()
browser.find_element_by_id("TPL_password_1").send_keys(password)
    #点击登录按钮
browser.find_element_by_id("J_SubmitStatic").click();
browser.switch_to.default_content()
    #检测URL是否已经变化，变化我就认为登录成功，简单点嘛
while True:
    if browser.current_url != url:
        break
    time.sleep(1)
    #cookie取到了
cookie = "; ".join([item["name"] + "=" + item["value"] for item in browser.get_cookies()])
       #关闭浏览器'''
browser.quit()