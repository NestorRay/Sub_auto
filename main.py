import os
import logging
from pickle import NONE
import requests
import socketserver
import time

#获取时间，写入日志
def time_now():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return t

#设置环境代理
socks5_proxy="127.0.0.1:7890"

# os.system("pip3 install -r ./requirement.txt")

#连通性测试
url="https://api.github.com/"
content=requests.get(url).content
#判断返回值是否为空
if content is not NONE:
    print(time_now(),"连通性测试成功")
else:
    print(time_now(),"测试失败")