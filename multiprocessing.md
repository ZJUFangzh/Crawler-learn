#多进程

```py
from multiprocessing import Pool



pool = Pool(processes=4)  #也可自动分配，不写参数
pool.map(func,link_list.split())   #将 后面的那些链接列表一个个传入func中




```