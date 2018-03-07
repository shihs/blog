---
layout: post
title: "[Python][爬蟲]不同的 Content-Type (application/json)"
date: 2017-05-05 15:45
author: "Shihs"
category: Python
---

目標是爬取 http://waste.epa.gov.tw/WasteConfigure/VocationCode.asp<br>
所有的行業代碼與中文名稱。

按下一頁發現會load一個post的網址<br>
![螢幕快照 2017-05-10 下午3.47.28.png](http://user-image.logdown.io/user/13067/blog/12306/post/1792968/fSvGMaRQRCfVLL1T7SMz_%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202017-05-10%20%E4%B8%8B%E5%8D%883.47.28.png)


接著想要在headers裡找到 "Form Data"，<br>
這裡面應會藏著post需要的參數。<br>

可是，這時候卻只有找到 "Requests Payload"，<br>
這個看起來很像payload的東西，<br>
它看起來是個json，<br>
且Response Headers的Content-Type正是application/json。

![content type.png](http://user-image.logdown.io/user/13067/blog/12306/post/1792968/qomn6tsmQcaYV27GsYea_content%20type.png)

所以我將 "Requests Payload"按下view source後的結果直接複製，<br>
然後requests結果再用json.loads就可以得到想要的結果了。<br>

程式碼如下，

```python
# -*- coding:utf-8 -*-
# 爬取 http://waste.epa.gov.tw/WasteConfigure/VocationCode.asp 行業代碼(4碼)
import requests
import json


# payload for requests
payload = '{"Cond":{"KeyWord":"","Paging":{"Size":519,"Current":1,"Count":52,"RecordCount":519,"CanPrev":false,"CanNext":true}}}'

headers = {"Content-Type":"application/json", 
		  "Referer":"http://waste.epa.gov.tw/WasteConfigure/VocationCode.asp"}

url = "http://waste.epa.gov.tw/NRS40/_ws/JsApI/CodeQuery.asmx/Vocation"

res = requests.post(url, data = payload, headers = headers)

js = json.loads(res.text)

for i in js["d"]["Result"]:
	code = i["Code"]
	name = i["Name"].encode("utf-8", "ignore")
	print code

```