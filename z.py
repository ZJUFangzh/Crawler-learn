from selenium import webdriver
import io
import sys

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
browser = webdriver.Chrome()
browser.get('http://www.taobao.com')

a = browser.page_source.encode('utf-8').decode()

print(a)
