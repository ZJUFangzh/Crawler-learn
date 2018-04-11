#Mongodb

```py
import pymongo


client = pymongo.MongoClient('localhost',27017)  #链接数据库
walden = client['walden']    #创建一个数据库
sheet_lines = walden['sheet_lines']  #在库中创建一个表
data = {'':'','':''}
sheet_lines.insert(data) #插入



for item in sheet_lines.find():
    print(item)



#  $lt/$lte/$gt/$gte/$ne     </<=/>/>=/!=     g:greater   e :equal  n:not
for item in sheet_lines.find(key:''):   #找特定元素      {'words':{'$lt':5}}  筛选出words小于5的   lt:less than
    print(item)
    print(item['line'])



#{id:1,name:0,info:3}
db.collection.update({id:1},{$set:{name:2}})
db.collection.find({id:1},{name:1,info:1})      #后半段为想看的字段中的那些元素，1为想看，0位不想看.  前半段是指定哪些字段
db.collection.aggregate(pipeline)    #管道模型
 
pipeline=[
    {'$match':{key:value}}
]
 
pipeline=[
    {'$match':{'$and':[{k:v},{k:v}]}}   #与运算
    {'$group':{'_id':'$price','counts':{'$sum':1}}}
    {'$sort' :{'counts':1}}                   # 1 表示 从小到大
    {'$limit':3}       #限制查找数量
]










```