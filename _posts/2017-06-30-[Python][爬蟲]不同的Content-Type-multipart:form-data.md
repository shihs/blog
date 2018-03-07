---
layout: post
title: "[Python][爬蟲]不同的 Content-Type (multipart/form-data)"
date: 2017-06-30 10:26
author: "Shihs"
category: R
---

這次要爬的目標是[台灣精品獎得獎名單](http://www.taiwanexcellence.org/index.php/awards/now/cross/1)。<br>

我想要爬取的條件是，
![擷取.PNG](http://user-image.logdown.io/user/13067/blog/12306/post/1985162/Hpw8hdtgR2y2Yr1gIYln_%E6%93%B7%E5%8F%96.PNG)

這時候會猜測這應該是個post的requests。

果然，在按下查詢後，<br>
出現了一個cross_list的可疑人物，<br>
![擷取.PNG](http://user-image.logdown.io/user/13067/blog/12306/post/1985162/iJbMP5kdRba31P5IoKG0_%E6%93%B7%E5%8F%96.PNG)

因為是post，<br>
所以會期望在headers裡找到 "Form Data"，<br>
這裡面應會藏著post需要的參數。<br>

但不幸的是，什麼也沒有，<br>
只找到長得像這樣的"Request Payload"<br>
![payload.PNG](http://user-image.logdown.io/user/13067/blog/12306/post/1985162/w5DjcxhTR0s2PKSNbQwQ_payload.PNG)

然後Content-Type是multipart/form-data<br>
![content-type.PNG](http://user-image.logdown.io/user/13067/blog/12306/post/1985162/SEe7tcApQfCSkEeYEgml_content-type.PNG)


其實，我們平常需要的data form裡的資料就藏在Request Payload裡。<br>
抓取的方式是，<br>
![payload.PNG](http://user-image.logdown.io/user/13067/blog/12306/post/1985162/w5DjcxhTR0s2PKSNbQwQ_payload.PNG)

以這行為例，
```
------WebKitFormBoundaryTaDJAA82fTd3ug3W
Content-Disposition: form-data; name="awards[]"

1
```
name後的 "award[]" 就會是dictionary的key，
底下的 1 ，就會是value，
所以就會變成
```python
{
"awards[]" = "1"
}
```

所以就把Request Payload所有的資訊寫成
```python
payload = {
	"keyword":"",
	"awards[]":"1",
	"awards[]":"2",
	"awards[]":"3",
	"years[]":"2017",
	"years[]":"2016",
	"industry[]":"A",
	"industry[]":"B",
	"industry[]":"C",
	"industry[]":"D",
	"industry[]":"E",
	"industry[]":"F",
	"industry[]":"G",
	"industry[]":"H",
	"industry[]":"I",
	"industry[]":"J",
	"industry[]":"K",
	"industry[]":"L",
	"industry[]":"Z"
}
```

但這樣寫完會覺得非常不合理，<br>
因為會有一堆同樣的key但給予不同的value，<br>
也就是說會key會一直被新的value取代。<br>

我當時的想法是，<br>
看到 [] 就會很想要在裡面塞數字順位，<br>
果然，從0開始，將相同的key編號，<br>
就成功了。<br>


所以這樣送出requests，
```python
# -*- coding: utf-8 -*-
#爬取台灣精品得獎名單http://www.taiwanexcellence.org/index.php/awards/now/cross_list/1/2017/2/1
from bs4 import BeautifulSoup
import requests
import math


url = "http://www.taiwanexcellence.org/index.php/awards/now/send_search/1/2017/2/1/cross_list"

payload = {
	"keyword":"",
	"awards[0]":"1",
	"awards[1]":"2",
	"awards[2]":"3",
	"years[0]":"2017",
	"years[1]":"2016",
	"industry[0]":"A",
	"industry[1]":"B",
	"industry[2]":"C",
	"industry[3]":"D",
	"industry[4]":"E",
	"industry[5]":"F",
	"industry[6]":"G",
	"industry[7]":"H",
	"industry[8]":"I",
	"industry[9]":"J",
	"industry[10]":"K",
	"industry[11]":"L",
	"industry[12]":"Z"
}

s = requests.Session()
res = s.post(url, data = payload)

```

[完整的代碼](https://github.com/shihs/crawlers/blob/master/%E5%8F%B0%E7%81%A3%E7%B2%BE%E5%93%81%E7%8D%8E/taiwanexcellence.py)




