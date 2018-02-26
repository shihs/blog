---
layout: post
title: "[Python][爬蟲]防止被ban，代理IP怎麼用?"
date: 2018-02-07 11:47
author: "Shihs"
---

<!--break-->

## **如何讓爬蟲程式不被ban?**
1. 動態設置user agent
2. 使用代理IP

<!--break-->

[參考](http://willdrevo.com/using-a-proxy-with-a-randomized-user-agent-in-python-requests)<br>
這裡主要介紹如何使用IP代理。

## **proxy代理類型** 
[參考](http://gohom.win/2016/01/20/proxy-type/)
1. 透明代理(Transparent Proxy)<br>
REMOTE_ADDR = Proxy IP<br>
HTTP_VIA = Proxy IP<br>
HTTP_X_FORWARDED_FOR = Your IP

2. 匿名代理(Anonymous Proxy)<br>
REMOTE_ADDR = proxy IP<br>
HTTP_VIA = proxy IP<br>
HTTP_X_FORWARDED_FOR = proxy IP

3. 混淆代理(Distorting Proxies)<br>
REMOTE_ADDR = Proxy IP<br>
HTTP_VIA = Proxy IP<br>
HTTP_X_FORWARDED_FOR = Random IP address

4. 高匿代理(Elite proxy或High Anonymity Proxy)<br>
REMOTE_ADDR = Proxy IP<br>
HTTP_VIA = not determined<br>
HTTP_X_FORWARDED_FOR = not determined<br>




## **代理proxy哪裡找？**
這裡提供兩個我覺得品質比較好的proxy代理<br>
1. http://www.goubanjia.com/free/index.shtml<br>
2. http://www.proxyserverlist24.top/<br>

[程式碼](https://github.com/shihs/proxy/blob/master/get_proxies.py)


## **如何確定真的使用代理IP了？**
```python
import requests

# 隨便google可以找到可以查詢自己IP的網站

url = "http://icanhazip.com/"  # 這個網站可以知道目前瀏覽的IP
proxies = {
	"http":"http://xx.xx.xxx:xxxx",
	"https":"https://xx.xx.xxx:xxxx",

}
###注意
#要爬取的網站是使用什麼協定？http？https？
#網址可能會有轉址的情況，最後轉的那個網址才是真正的協定喔

res = requests.get(url, proxies = proxies)
print res.text  # 如果這個網站print出來的和proxies一樣，那就表示成功了


```


抓完proxy後，我將所有proxy儲存在csv檔案中，
要爬取網站的時候，先讀取該檔案，
只要被擋，就random使用proxy替換proxies。

如果所有proxy都用完再重新爬取，
網站上的proxy都會不停更換，
所以只要更新proxy庫就好。

