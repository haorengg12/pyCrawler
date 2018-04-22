# coding=utf-8
# 用来进行文件测试
import os

import requests


def testPath(tpath, tmode):  # 测试文件读写权限
    print os.access(tpath, tmode)  # os.access('C:/Users/ASUS/untitled2/kk', os.R_OK)


def testDown(path):  # 测试是否能下载到指定目录
    print 'start'
    res = requests.get('https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86_64.exe',{'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'})
    with open(path + '/kk.exe', 'wb') as f:
        f.write(res.content)
        f.close()
        print 'done\n'


if __name__ == '__main__':
    mode1 = os.F_OK  # 测试path是否存在
    mode2 = os.R_OK  # 测试path是否可读
    mode3 = os.W_OK  # 测试path是否可写
    mode4 = os.X_OK  # 测试path是否可执行
    path1 = '../kk'
    testPath(path1, mode1)
    # testPath(path2, mode1)
    testPath(path1, mode4)
    testDown(path1)
