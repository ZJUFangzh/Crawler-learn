# pictures
# 注意headers

import requests
import os
root = 'D://'
url = 'http://img0.dili360.com/rw9/ga/M01/49/B7/wKgBzFqo8FiAbCQlAAWcL5cYgHI592.tub.jpg'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36', }
path = root + url.split('/')[-1]

r = requests.get(url, headers=headers)


with open(path, 'wb+') as f:
    f.write(r.content)
