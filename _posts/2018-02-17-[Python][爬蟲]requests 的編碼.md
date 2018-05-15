---
layout: post
title: "[Python][爬蟲]requests 的編碼"
date: 2018-02-17 19:01
author: "Shihs"
category: [Python, 爬蟲]
---

```
rep = requests.get(url)
```
**rep.content ： bytes 型別**

**rep.text    ： unicode 型別**<br>
1.是由 requests 以 rep.encoding 自動轉換的！<br>
2.rep.encoding 是以 Reponse Headers 的 Content-Type 決定！

