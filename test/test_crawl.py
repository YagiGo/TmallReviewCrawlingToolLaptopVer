# 导入所需的开发模块
import requests
import re
# 创建循环链接
urls = []
for i in list(range(1,50)):
    urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=521136254098&spuId=345965243&sellerId=2106525799&order=1&currentPage=%s' %i)
# 构建字段容器
username = []
ratedate = []
#color = []
#size = []
ratecontent = []
# 循环抓取数据
for url in urls:
    content = requests.get(url).text

# 借助正则表达式使用findall进行匹配查询
    username.extend(re.findall('"displayUserNick":"(.*?)"',content))
    #color.extend(re.findall(re.compile('颜色分类:(.*?);'),content))
    #size.extend(re.findall(re.compile('尺码:(.*?);'),content))
    ratecontent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'),content))
    ratedate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'),content))
    print(username,ratedate)

# 写入数据
file = open('review of Xiaomi5s.csv','w')
for i in list(range(0,len(username))):
    file.write(','.join((username[i],ratedate[i],ratecontent[i]))+'\n')
file.close()