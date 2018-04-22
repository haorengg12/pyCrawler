# coding=utf-8
# 线程测试(误)
def tt1(k):
    tt2(k)
    return k


def tt2(i):
    print "tt2:" + i
    return


if __name__ == '__main__':
    i = '1'
    print tt1(i)
