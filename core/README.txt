使用模块Selenium，request，time，OS，BeautifulSoup
！使用项目IPProxy来爬取IP代理供爬虫使用，请先下载IPProxy项目运行后再运行本项目！
https://github.com/qiyeboy/IPProxyPool


基于python3.5
使用之前需要把chromedriver加载到环境变量
-win系统直接编辑环境变量
-mac/linux把chromedriver.exe添加到/usr/bin中
各文件用途

MySQL.py 用于创建和修改保存商品评论的数据库 TODO
getHTML.py 使用Selenium自动对指定关键字搜索得到的商品网页进行抓取，得到网页的HTML源码，用于获取商品ID。
detectCAPTCHA.py 在getHTML.py运行过程中检测是否触发了验证码，如果触发，则进行处理  
                 商品关键字和搜索页数由用户指定
searchProducts.py 输入通过getHTML获得的html源文件，从中查找并且保存所有的商品ID，用于getReview.py获取商品评论
getReview.py 用于获取商品评论。其中包含数个函数：
            checkIfCAPTCHATriggered(content) 判断在读取评论的过程中是否触发验证码，如果出发返回特定值，如果没有出发，返回空数组
            saveReview 保存得到的评论。可以保存某一商品制定的所有页数的评论。如果评论总数少于用户输入的页数，则爬去商品的所有评论。及某一商品的评论  
            页数不会超过用户指定的页数
            getReview 获得由getHTML函数得到的全部网页中的商品的评论，使用saveReview函数保存
searchProducts.py 输入通过getHTML获得的html源文件，从中查找并且保存所有的商品ID，用于getReview.py获取商品评论
/**********************************************测试用途的文件****************************/
createDatabase.py
single-thread T-mall.py
testGround.py 代码测试用，正确无误后插入正式文件
/**********************************************测试用途的文件**************************/
