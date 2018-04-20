# coding=utf-8
# get music from http://www.luoo.net/music/680
# TODO:屏蔽无关项 防止git上去
from string import maketrans

import os
import requests
from bs4 import BeautifulSoup
from faker import Factory

fake = Factory.create()
luoo_site_mp3 = 'http://mp3-cdn2.luoo.net/low/luoo/radio680/%s.mp3'
local_file2 = 'C:/Users/ASUS/untitled2/kk/%s.mp3'  # 写入时需要文件名

proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}  # 设置代理，需要安装
headers = {
    'Connection': 'keep-alive',
    'User-Agent': fake.user_agent()}


def tra(track_name):  # 合成链接
    intab = "a"
    outtab = "a"
    trantab = maketrans(intab, outtab)
    track_name4 = (track_name[3].text)[0:2]
    track_link = str(luoo_site_mp3 % (track_name4)).translate(trantab, ' ')
    return track_link


def linkstart():
    res = requests.get("http://www.luoo.net/music/680", proxies=proxies)
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup


def download(link):  # 下载
    print "start download in", local_file2
    res = requests.get(link, proxies=proxies, headers=headers)
    with open(local_file2, 'wb') as f:
        f.write(res.content)
        f.close()
        print 'download finish !\n'


if __name__ == '__main__':
    soup = linkstart()  # 开始连接
    title = soup.find('span', attrs={'class': 'vol-title'}).text
    print "Title", title
    num = soup.find('span', attrs={'class': 'vol-number rounded'}).text
    print "序号", num
    cover = soup.find('img', attrs={'class': 'vol-cover'})['src']
    desc = soup.find('div', attrs={'class': 'vol-desc'})
    track_names = soup.findAll('a', attrs={'class': 'trackname btn-play'})  # 判断歌曲数量的基准
    track_count = len(track_names)  # music 数量
    track_link = tra(track_names)
    print os.access('C:/Users/ASUS/untitled2/kk', os.R_OK)
    download(track_link)  # 下载
