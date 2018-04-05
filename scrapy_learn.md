#scrapy爬虫框架 5+2结构

##Engine
框架的核心，不需要用户修改

- 控制所有模块之间的数据流
- 根据条件触发事件

##Downloader
- 根据请求下载网页，不需要修改

##Scheduler
- 对爬取的请求进行调度管理，不需要修改

##**Downloader Middleware**模块
- 对Engine,Scheduler,Downloader之间进行用户可配置的控制
- 功能：可以对这个模块的编写，修改、丢弃、新增请求响应

##Spider
最核心，需要配置

- 解析Dowloader返回的响应(Response)
- 产生爬取项（scraped item）
- 产生额外的爬取请求（Request）

##Item Pipelines 
- 流水线处理Spider 产生的爬取项
- 由一组操作顺序组成，每一个都是Item Pipelines 类型
- 可以用来清理、检验、查重、储存到数据库，需要配置代码

##**Spider Middleware**模块
- 目的：对请求和爬取项再处理，可以配置代码
- 功能：修改、丢弃、新增请求或者爬取项






##常用命令，用命令行()scrapy -h
- startproject 创建工程
- genspider  创建爬虫
- settings  配置爬虫信息
- crawl 运行一个爬虫
- list   列出所有爬虫
- shell   启动URL调试命令行




##数据类型

**Request类**
由Spider生成，Downloader执行

    .url
    .methond
    .headers
    .body
    .meta
    .copy()

**Response类**
由Downloader 生成，Spider处理

    .url
    .status     200
    .headers
    .body
    .flags
    .request   对应的request对象
    .copy()

**Item类**
从HTML页面中提取的信息内容
由Spider生成，由Item Pipeline处理
类字典类型

CSS Selector

    <HTML>.css('a::attr(href)').extract()
