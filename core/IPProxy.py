#! /usr/bin/env python
# -*- coding utf-8 -*-
#使用开源库IPProxyPool获取了足够的IP地址，用于对抗反爬虫
import requests as rq
import json
import random
def getIPProxies():
    url = 'http://127.0.0.1:8000'
    IPAddr = rq.get(url).text
    IPPorts = json.loads(IPAddr)
    max = len(IPPorts)
    item = random.randint(0 , max-1)
    ip = IPPorts[item][0]
    port = IPPorts[item][1]
    proxies = {
        'http': 'http://{}:{}'.format(ip,port),
        'https': 'https://{}:{}'.format(ip,port)
    }
    print("使用代理{}".format(proxies)) #验证是否可以成功使用
    return proxies