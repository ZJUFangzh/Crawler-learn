# 股票数据
# requests re soup
'''
1、东方财富网获取列表
2、逐个去百度股票获取个股信息
3、将结果储存到文件中

'''
import requests
from bs4 import BeautifulSoup
import traceback
import re
import sys
import io


def getHTMLText(url):

    r = requests.get(url)
#        r.raise_for_status()
    r.encoding = r.apparent_encoding

    return r.text


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', attrs={'class': 'quotebody'})
    a = div.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
#            print(' ')
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
#            print('getStockList ok')
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + '.html'
        html = getHTMLText(url)
        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                print('s')
        except:
            print('this')
            traceback.print_exc()
            continue


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36', }
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://gupiao.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)



#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
main()
