#Selenium

```py
from selenium import webdriver


browser = webdriver.Chrome()
browser.get(url)
print(browser.page_source)
browser.close()
```


    input = browser.find_element_by_id('q')
    input = browser.find_element_by_css_selector('#q')
    _by_name   link_text  tag_name  class_name  等等

也可以用

    from selenium.webdriver.common.by import By
    browser.find_element(By.ID,'q')

多个元素：

    input = browser.find_elements_by_id('q')



交互 

    input = browser.find_element_by_id('q')
    input.send_keys('iphone')
    input.clear()
    input.send_keys('ipad')
    botton = brower.find_element_by_class_name('btn-search')
    button.click()

交互动作      
鼠标拖拽
action chains


##执行JavaScript

    browser.execute_script('')


获取属性

    input = browser.find_element_by_id('q')
    input.get_attribute('class')

获取文本值

    input = browser.find_element_by_id('q')
    input.text


获取id 位置 标签名 大小

    input.id
    .location
    .tag_name
    .size


