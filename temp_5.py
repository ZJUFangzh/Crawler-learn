# IP地址归属地查询
# http://www.ip138.com/ips138.asp?ip= address


import requests
url = 'http://www.ip138.com/ips138.asp?ip='
try:
    r = requests.get(url + 'www.cc98.org')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-3000:-500])
except:
    print('failed')
