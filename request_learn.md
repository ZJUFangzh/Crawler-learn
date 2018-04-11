#requests

    import requests

##r = requests.get(url)
```
# 200 or 404，判断是否是200
r.status_code

# 响应内容的字符串格式
r.text

# 从header中猜测响应内容的编码方式(ISO-8859-1，无法解析中文)
r.encoding

# 备选编码方式,根据内容部分，更加准确
r.apparent_encoding

# 响应内容的二进制形式，图片之类的
r.content


r.json
r.cookies
```

##异常处理
```python
requests.ConnectionError
requests.HTTPError
requests.URLRequired
requests.TooManyRedirects
requests.ConnectTimeout
requests.Timeout
r.raise_for_status()  # 如果200，正常，否则产生HTTPError
```

## 通用处理框架
```python
import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


url = "http://www.baidu.com"
print(getHTMLText(url))
```


##HTTP协议
GET   获取
HEAD  获取头部
POST   请求后附加新的数据
PUT  请求存储一个资源，覆盖原来，覆盖全部
PATCH  局部改变，可节省网络带宽
DELETE  删除


##requests.request(method, url, **kwargs)



method: 请求方式
**kwargs: 13个控制参数
params: 字典，字节序列，增加到URL中
data：字典、字节序列文件对象，去提交
json：去提交
headers：HTTP定制头
cookies
auth：元组
files：字典类型，传输文件
timeout：超时时间,为秒
prixies：字典类型，代理服务器
allow_redirects：重定向
stream：获取内容是否下载
verify：SSL认证 ，默认为True  如果改为False可以跳过验证，如12306，也可以用cert指定一个证书
cert：ssl路径



## 七个类，最常使用get和head
```
requests.get(url, params=None, **kwargs)

requests.head(url, **kwargs)

requests.post(url, data=None, json=None, **kwargs)

requests.put(url, data=None, **kwargs)

requests.patch(url, data=None, **kwargs)

requests.delete(url, **kwargs)

```

小规模：requests
中规模：scrapy
大规模：搜索引擎，定制

限制：
来源审查：User-Agent
发布公告：Robots协议
url/robots.txt


测试网址
    http://httpbin.org/


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36', }

Session可变成同一个对象进行多次请求
    s = requests.Session()    
    r = s.get()


安装socks代理

```
pip install requests[socks]
```

