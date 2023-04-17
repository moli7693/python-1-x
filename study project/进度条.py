from cgi import print_arguments
from time import time


c='64%'
b='{********************............}\n'
a='================开始下载================\n'
print(a,c,b)

print(a,(c.replace('64','100')),(b.replace('.','*')),(a.replace('开始下载','下载完成')))