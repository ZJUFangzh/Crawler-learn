# 京东


import requests

url = 'https://item.jd.com/6856234.html'

r = requests.get(url)

a = r.status_code
b = r.encoding

print(r.text)
