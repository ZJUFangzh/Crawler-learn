# baidu 360
# http://www.baidu.com/s?wd=keyword
# http://www.baidu.com/s?q=keyword
#
import requests
kv = {'wd': 'Python'}

try:
    r = requests.get('http://www.baidu.com/s', params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('error')
