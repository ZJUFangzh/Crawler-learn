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
