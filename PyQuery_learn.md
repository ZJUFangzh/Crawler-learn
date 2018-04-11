#Pyquery


字符串初始化

    from pyquery import PyQuery as pq
    doc = pq(html)
    print(doc('li'))

URL 初始化

    doc = pq(url)
    print(doc('head'))


文件初始化
    
    doc = pq(filename='')

CSS选择器

    doc('#container .list  li')


查找元素

子元素,都是 PyQuery对象

    items = doc('.list')
    lis = items.find('li')

    items.children('')
    items.parent('')
    items.parents('')
    items.siblings('')


遍历

    list = doc('li').items()
    for li in list:
        print(li)


获取信息


获取属性

    a = doc('')
    a.attr.href
    a.attr('href')


获取文本

    a.text()

获取html
    
    a.html()


DOM操作

    addClass('')
    removeClass


    li.attr('name','link')
    li.css('font-size','14px')


    li.find('p').remove()