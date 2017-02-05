# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import commands
import datetime
import time

hour_list = range(24)

while len(hour_list) != 0:
    current_hour = datetime.datetime.now().hour
    if current_hour in hour_list:
        req = requests.get('http://m.baidu.com/s?word=ip')
        html = BeautifulSoup(req.content, 'html.parser')
        ip = html.find_all(text=re.compile(u'本机IP:'))[0].split(':')[-1]
        status, info = commands.getstatusoutput("ssh root@conj.space 'cd /home/env; python update_ip.py %s'" % ip)
        print status, info
        hour_list.remove(current_hour)
    time.sleep(60*30)


