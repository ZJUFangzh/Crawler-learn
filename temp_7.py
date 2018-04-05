# 淘宝 比价

'''
1.淘宝搜索接口
2.翻页处理
用requests-re


1.提交搜索请求，循环获取页面
2.对每个页面，提取商品名称和价格
3.输出到屏幕上
'''

import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


def parsePage(ilt, html):
    try:
        plt = re.findall(r'"view_price":"[\d.]*"', html)
        tlt = re.findall(r'"raw_title":".*?"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[-1])
            title = eval(tlt[i].split(':')[-1])
            ilt.append([price, title])
    except:
        print('')


def printList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))


def main():
    good = 'c++primer'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + good
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printList(infoList)


main()
