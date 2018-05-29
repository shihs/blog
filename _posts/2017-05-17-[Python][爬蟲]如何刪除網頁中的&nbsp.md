---
layout: post
comments: true
title: "[Python][爬蟲]如何刪除網頁中的&nbsp"
date: 2017-05-17 15:23
author: "Shihs"
category: [Python, 爬蟲]
---


在爬取網頁時偶爾會碰到<br>

```html
&nbsp;
```

而且怎麼樣都刪不掉也取代不掉，<br>
使用strip()仍然會有空白。


```
「&nbsp;」 是屬於 HTML 的特殊符號之一「空格符號」，其 nbsp 取自於英文 a non-breaking space 的英文簡稱，其原意是「不會被間斷的空白」
```


假如現在有一個網頁內容包含

```html
<td>
	E601010&nbsp;
	電器承裝業
	<br>
	E601020&nbsp;
	電器安裝業
	<br>													
</td>
```

已經抓出td tag，<br>
接著可以使用

```python
td = td.encode(formatter="html")
```
這時候td type會變成str，<br>
再使用replace取代就可以刪除空白了。<br>




