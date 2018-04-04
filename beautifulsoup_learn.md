#BeautifulSoup

    from bs4 import BeautifulSoup


## 解析器
html.parser
lxml
xml
html5lib(pip 这个库)


## 基本元素
Tag <> < / >   soup.a
Name < p > < / p > 'p'is name < tag > .name
Attributes  属性，字典形式，< tag > .attrs < p class....... >
NavigableString  非属性字符串 < tag > .string
Comment  字符串中的注释部分


##下行遍历

.contents      子节点列表，所有儿子节点
.children  子节点迭代，循环遍历儿子节点
.descendants   子孙节点 循环遍历

    soup = BeautifulSoup(demo, 'html.parser')


## 上行遍历

.parent
.parents  所有先辈，可以循环遍历


## 平行遍历,同一个父节点下


.next_sibling 	下一个平行节点，有可能不是tag类型
.previous_sibling  上一个平行节点
.next_siblings
.previous_siblings


## 信息标记

XML <> < / >
JSON[{key: value}]
YAML  缩进


##信息提取

    <>.find_all(name,attrs,recursive,string,**kwargs)
返回一个列表类型，储存查找结果

name:
```py
import requests
from bs4 import BeautifulSoup


url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
# 获得文本后先在BS库中解析
soup = BeautifulSoup(demo, 'html.parser')
soup.find_all('a')
soup.find_all(['a','b'])
#可输入正则表达式
```
attrs:  检索属性值
recursive : 默认情况True ，遍历子孙节点
string： 检索字符串
<>()   =  <>.find_all()
<>.find()  只返回一个结果，为字符串格式


中文空格 chr(12288)
