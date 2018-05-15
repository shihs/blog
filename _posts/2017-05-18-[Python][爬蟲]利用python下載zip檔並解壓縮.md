---
layout: post
title: "[Python][爬蟲]利用python下載zip檔並解壓縮"
date: 2017-05-18 16:19
author: "Shihs"
category: [Python, 爬蟲]
---

下載檔案是使用package urllib2<br>
解壓縮檔案則是使用package zipfile<br>

```python
# 下載與解壓縮 財政部財政資訊中心-全國營業(稅籍)登記資料集 http://data.gov.tw/node/9400
import urllib2 #urllib2.urlopen 
import zipfile #zipfile.ZipFile

def DownloadTWCompany():
	# 檔案下載
	print "下載全國營業(稅籍)登記資料集壓縮擋..."
	downloadurl = urllib2.urlopen('http://www.fia.gov.tw/opendata/bgmopen1.zip')
	zipcontent= downloadurl.read()
	with open("TWRAW.zip", 'wb') as f:
	    f.write(zipcontent)
	print "下載完成!"
	
	# 解壓縮檔案
	print "資料解壓縮..."
	with zipfile.ZipFile(open('TWRAW.zip', 'rb')) as f:
		f.extractall(".", pwd = "1234")  # 解壓縮密碼1234
	
	print "解壓縮完成!"

DownloadTWCompany()

```

