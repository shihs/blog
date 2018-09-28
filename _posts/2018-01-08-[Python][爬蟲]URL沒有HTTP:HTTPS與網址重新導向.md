---
layout: post
comments: true
title: "[Python][爬蟲]URL沒有 HTTP/HTTPS 與網址重新導向"
date: 2018-01-08 15:12
author: "Shihs"
category: [Python, 爬蟲]
---

這次要爬的網址長得像這樣
- hazyfairyland.blogspot.tw
- cartersoshkosh.tw
- yungmaun.com.tw

沒有www也沒有[http/https](https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%AE%89%E5%85%A8%E5%8D%8F%E8%AE%AE){:target="_blank"}，<br>
如果直接將這樣的網址丟到瀏覽器的網址列它會自動重新導向，<br>
但如果是使用request就會產生錯誤訊息。<br>

這時候該怎麼辦呢？

其實只要在前方加上"http://"就行了，<br>
若其實該網址是"https//"， request也會自動重新導向。<br>

假如所有的網址都是沒有www，<br>
就直接在所有url前方加上"http://"就好了。<br>


```python
url = "cartersoshkosh.tw"

while True:
    try:
        res = requests.get(url, timeout = 30)		
        break
			
    # catch requests.exceptions.MissingSchema error, add "http://" in the front
    except requests.exceptions.MissingSchema:
        url = "http://" + url
       
    print res.url  # print the final url
    print res.history  # print how many redirections it has gone throgh
```

