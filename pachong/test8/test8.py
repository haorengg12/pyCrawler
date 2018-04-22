# coding=utf-8
# python2.7
import requests

url = 'https://www.facebook.com'
response = requests.get(url=url)
print response
# <Response [200]>
# 注：200就是连接上了
