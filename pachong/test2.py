# coding=utf-8
# get music from http://www.luoo.net/music/*
from string import maketrans

import os
import requests
from bs4 import BeautifulSoup
from faker import Factory

fake = Factory.create()
luoo_site = 'http://www.luoo.net/music/%s'  # 文章地址模板
luoo_site_mp3 = 'http://mp3-cdn2.luoo.net/low/luoo/radio%s/%s.mp3'  # 音乐文件的源模板
local_file = 'C:/Users/ASUS/untitled2/kk/%s.mp3'  # 本地文件名模板

proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}  # 设置代理，需要安装
headers = {
    'Connection': 'keep-alive',
    'User-Agent': fake.user_agent()}


def linkstart(link_num):
    linknum = str(link_num)  # 接听用户输入的文章号
    site = str(luoo_site % (linknum))  # 获取的文章链接
    res = requests.get(site, proxies=proxies)  # get到的网页
    return res  # 返回的网页


def download(num, tracknames, link_num):  # 下载
    # TODO:多线程下载,顺便如果没有文件夹，新建文件夹
    print "Start download ! "
    for i in range(num):
        print "Download",track_names[i].text
        path = tra(tracknames[i].text)  # 修改文件名
        link = llink(track_names[i].text, link_num)  # 合成link
        res = requests.get(link, proxies=proxies, headers=headers)
        with open(path, 'wb') as f:  # 写入文件
            f.write(res.content)
            f.close()

    print 'Download finish !\n'
    exit(0)


def llink(track_name, link_num):  # make the download link
    track_name = track_name[0:2]
    link = luoo_site_mp3 % (link_num, track_name)
    return link


def tra(track_name):  # make local path
    # intab = "a"
    # outtab = "a"
    # trantab = maketrans(intab, outtab)
    # track_link = str(luoo_site_mp3 % (link_num, track_name4)).translate(trantab, ' ')
    path = local_file % (track_name)
    return path


if __name__ == '__main__':
    link_num = raw_input("Please input the music number:")  # 用户输入的数字
    res = linkstart(link_num)  # 开始连接
    # TODO:模块 或者 精简
    soup = BeautifulSoup(res.content, 'html.parser')  # 解释网页-》soup
    title = soup.find('span', attrs={'class': 'vol-title'}).text  # 标题，可以当做文件夹名字
    cover = soup.find('img', attrs={'class': 'vol-cover'})['src']  # 图片
    desc = soup.find('div', attrs={'class': 'vol-desc'}).text  # 文章的解说
    track_names = soup.findAll('a', attrs={'class': 'trackname btn-play'})  # 判断歌曲数量的基准
    track_count = len(track_names)  # 歌曲 数量
    # 准备下载
    download(track_count, track_names, link_num)  # 下载
