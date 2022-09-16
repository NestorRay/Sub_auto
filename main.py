from fileinput import filename
import os
import logging
import urllib
from pickle import NONE
import requests
import socketserver
import time

#创建日志文件并写入
def logs (t,cont):
    filename='log.txt'
    with open(filename,'a') as f:
        cont=time_now()+" "+cont
        f.write(cont)
#获取时间，写入日志
def time_now():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return t

#定义覆盖配置文件函数
def config(content):
    filename='Subconverter.yaml'
    with open(filename,'w',encoding='UTF-8') as c:
        c.write(content)

#设置环境代理
socks5_proxy="127.0.0.1:7890"

# os.system("pip3 install -r ./requirement.txt")

#连通性测试
url="https://api.github.com/"
content=requests.get(url).content
#判断返回值是否为空
if content is not NONE:
    logs(time_now(),"Connected to the proxy server\n")
else:
    logs(time_now(),"Cannot Connect to the proxy server\n")

#获取本地subconverter
url_sub="http://127.0.0.1:25500/sub?target=clash&url=https%3A%2F%2Fapi.ndsxfkjfvhzdsfio.quest%2Flink%2FmZLZLjiB65lrRCQ4%3Fclash%3D3%7Chttps%3A%2F%2Fxn--4gq62f52gdss.com%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3Dda50b2e73b47466297a62ee4dbad939e&config=https%3A%2F%2Fgist.github.com%2FNestorRay%2Fb9bca277317d0d6acaee858996e59605&append_type=true"
logs(time_now(),"Start Update\n")
content=requests.get(url_sub).content.decode("utf-8")
config(content)
logs(time_now(),"Update ended\n")