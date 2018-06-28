---
layout: post
comments: true
title: "Google Map API - Geocoding 地址經緯度"
date: 2018-06-28 14:10
author: "Shihs"
category: [Others, Python]
---

Google Map 提供了很多 [API](https://developers.google.com/maps/documentation/)，方便開發者根據自己的需求使用。不過大部分的 API 都需要使用 Google 帳號申請一個 API KEY 。 API KEY 申請時要填上信用卡資訊，有一年的免費使用時間，過了一年以後會自動扣款，但隨時都可以停用，而且時間快到時 Google 也會寄信通知你。

這次要介紹`Geocoding`這個 API 。 根據[說明文件](https://developers.google.com/maps/documentation/geocoding/intro)上的介紹
```
Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates (like latitude 37.423021 and longitude -122.083739), which you can use to place markers on a map, or position the map.
```
簡單來說，你可以**根據地址找到該地址在地理上的座標（經緯度）**，方便應用在地圖上標記位置。

根據`Geocoding`說明文件，這個 API 的 format 有 json 和 xml 兩種格式。
來看文件上給的一個輸出 json 格式的範例，
```
https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
```
看起來這個 API 是需要 API KEY 。

但其實，這個 API 是可以不需要 KEY 的。（我不知道為什麼 XD）
而且使用 API 還有限制一天可以搜尋的數量......

所以其實上面的例子只要這樣就好，
```
https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA
```
當然也可以搜尋中文地址，
```
https://maps.googleapis.com/maps/api/geocode/json?address=台北市中正區重慶南路一段122號
```
就可以獲取該地址完整的地址資訊（包括郵遞區號）與經緯度。
其實只要搜尋「重慶南路一段122號」就可以找到該地址完整的資訊了。


### 使用 python 快速爬取 API 內容 ###
這邊我寫了一個簡單的 python 程式可以快速地使用這個 API 獲得地址的經緯度。

```python
import requests
import urllib
import json

def get_latitude_longtitude(address):
    # decode url
    address = urllib.quote(address)
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address
    
    while True:
        res = requests.get(url)
        js = json.loads(res.text)

        if js["status"] != "OVER_QUERY_LIMIT":
            time.sleep(1)
            break

    result = js["results"][0]["geometry"]["location"]
    lat = result["lat"]
    lng = result["lng"]

    return lat, lng



address = "重慶南路一段122號"
lat, lng = get_latitude_longtitude()

```


























