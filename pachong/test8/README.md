# 关于在国内爬外网
## 解决过程

#### 一开始用这段代码完全不好使，开着shadowsocks（pac）也不行

    proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}
    url = 'https://www.facebook.com'
    response = requests.get(url=url, proxies=proxies, headers=headerss, timeout=10)
就是报这种错误

requests.exceptions.ConnectionError: HTTPSConnectionPool(host='www.facebook.com', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x0609DB10>: Failed to establish a new connection: [Errno 10061] ',))

#### 然后在github上
    用关键词 proxies = {'http': 'socks5://127.0.0.1:1080','https': 'socks5://127.0.0.1:1080'}
    搜索了很久 也都是千篇一律的 timeout 完全没有实际效果

#### 在以下的文上获得了启示

[一条来自于知乎上的评论](https://www.zhihu.com/question/52214600)

![](https://i.imgur.com/1ewVXkf.jpg)

[另一条来自于CSDN博主的文](https://blog.csdn.net/fangbinwei93/article/details/59526937)

![](https://i.imgur.com/28ZZlK2.jpg)

## 最后
解决办法：

    就是不要使用requests.get的proxies字段，就是不要挂socks5代理
    然后shadowsocks开全局（系统代理模式改为 全局模式）