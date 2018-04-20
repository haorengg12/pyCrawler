# coding=utf-8
from string import maketrans

import requests
from bs4 import BeautifulSoup
from faker import Factory

fake = Factory.create()
luoo_site_mp3 = 'http://mp3-cdn2.luoo.net/low/luoo/radio680/%s.mp3'
local_file2 = 'C:/Users/ASUS/untitled2/kk' #因为权限不够 无法写入
local_file = 'D:/kk/kk.mp3'

proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}  # 设置代理
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
    # print res.text
    soup = BeautifulSoup(res.content, 'html.parser')
    # print soup.div
    return soup


def download(link):
    print 'start download'
    res = requests.get(link, proxies=proxies, headers=headers)
    with open(local_file, 'wb') as f:
        f.write(res.content)
        f.close()
        print 'done\n'


if __name__ == '__main__':
    soup = linkstart()
    kurasi = soup.find(id="track12962")
    print kurasi
    title = soup.find('span', attrs={'class': 'vol-title'}).text
    print "Title是", title
    cover = soup.find('img', attrs={'class': 'vol-cover'})['src']
    desc = soup.find('div', attrs={'class': 'vol-desc'})
    track_names = soup.findAll('a', attrs={'class': 'trackname'})
    track_count = len(track_names)
    track_link = tra(track_names)
    download(track_link)
