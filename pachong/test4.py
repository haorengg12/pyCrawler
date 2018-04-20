# coding=utf-8
# 爬个校园网信息
import requests
from bs4 import BeautifulSoup, UnicodeDammit

res = requests.get("http://172.16.6.3")
soup = BeautifulSoup(res.content, 'html.parser')
kk = soup.find('script').text
print "使用时间", kk[12:20]
print "使用流量", str(int(kk[30:39]) / 1024) + '.' + str(int(float(kk[30:39]) % 1024)), "MB"
