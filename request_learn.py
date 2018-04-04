'''
尽管Requests库功能很友好、开发简单（其实除了import外只需一行主要代码），
但其性能与专业爬虫相比还是有一定差距的。请编写一个小程序，
“任意”找个url，测试一下成功爬取100次网页的时间。
（某些网站对于连续爬取页面将采取屏蔽IP的策略，所以，要避开这类网站。）
'''


import requests
import time


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return 'success'
    except:
        return 'error'


url = 'http://www.baidu.com'

t1 = time.time()
try:
    for i in range(100):
        getHTMLText(url)
    t2 = time.time()
    print(t2 - t1)
except:
    print('failed')
