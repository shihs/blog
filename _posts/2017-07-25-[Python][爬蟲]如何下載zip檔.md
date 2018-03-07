---
layout: post
title: "[Python][爬蟲]如何下載 zip 檔"
date: 2017-07-25 11:17
author: "Shihs"
category: Python
---

這裡要示範使用三個不同的package下載zip檔。

```python
import urllib
import urllib2
import requests

url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'

print "downloading with urllib"
urllib.urlretrieve(url, "code.zip")

print "downloading with urllib2"
f = urllib2.urlopen(url)
data = f.read()
with open("code2.zip", "wb") as code:
    code.write(data)

print "downloading with requests"
r = requests.get(url)
with open("code3.zip", "wb") as code:
    code.write(r.content)

```

[參考](https://dzone.com/articles/how-download-file-python)