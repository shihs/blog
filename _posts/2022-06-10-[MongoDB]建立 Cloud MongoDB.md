---
layout: post
comments: true
title: "[MongoDB]建立 Cloud MongoDB"
date: 2022-06-10 12:13
author: "Shihs"
category: [MongoDB]
---

## 使用 MongoDB Atlas 建立 Cloud MongoDB

- 註冊 [MongoDB Atlas](https://www.mongodb.com/atlas/database) 帳號
- 點選 **Sign In**
![](https://i.imgur.com/ZCctWhc.png)
- 登入
![](https://i.imgur.com/PUYzmMY.png)
- Accept Privacy Policy & Terms of Service
![](https://i.imgur.com/vf9T7rH.png)
- 問卷填寫
![](https://i.imgur.com/S7BKKOI.png)
- 選擇 deploy 的方案
![](https://i.imgur.com/uVWJMux.png)
- 選擇免費的方案 Create a Shared Cluster，這裡我是選擇 Google Cloud 在台灣的 Sever（要選擇其他 server 也可以），因為使用免費版本，所以其他設定都不調整，使用預設值，完成後選擇 **Create Cluster**
![](https://i.imgur.com/Eru5JEv.png)
![](https://i.imgur.com/MSDxbvm.png)
- 建立 Cluster 中
![](https://i.imgur.com/FaLtNCA.png)
- 設定 MongoDB 的 Username 和 Password
![](https://i.imgur.com/XILIeIx.png)
- 設定可連線 MongoDB 的 IP
![](https://i.imgur.com/P0TGWsz.png)
- Database Deployments
![](https://i.imgur.com/RHC7cAy.png)
- 載入 Sample Data 測試，點選 **Load Sample Data**，需要花點時間等待
![](https://i.imgur.com/OC9QQZV.png)
![](https://i.imgur.com/15nlBTB.png)
- Sample Data Loaded
- ![](https://i.imgur.com/OhUElwy.png)
- 查看資料，點選 **Browse Collection**，可以看到測試資料已經進到 MongoDB
![](https://i.imgur.com/7DBRFix.png)
- DB & Collection，以下圖為例，`sample_airbnb` 是 DB，`listingsAndReviews` 為 Collection
![](https://i.imgur.com/VlOC1Yf.png)
- 使用 Python 測試連線
接下來要示範連線至 listingsAndReviews 這個 Collection

## Connect MongoDB with Python
示範如何使用 Python 連剛剛建立的 Cloud MongoDB

### Install pymongo & dnspython
- `conda install pymongo`
- `conda install dnspython`

### 查看連線的 URI
- 點選 **Connect**
![](https://i.imgur.com/WENwjPR.png)
- 點選 **Connect your application**
![](https://i.imgur.com/6D025EI.png)
- 選擇 driver 的版本，這邊選擇 Python 3.6 含以上的版本，複製下方產生的程式碼，並將程式碼中的 `<password>` 改成剛剛設定的使用者的密碼
![](https://i.imgur.com/FMvaQcd.png)
- Python 程式碼示範

```python
from pymongo import MongoClient
import pprint

DB = 'sample_airbnb'
COLLECTION = 'listingsAndReviews'
URI = 'mongodb+srv://test:<password>@cluster0.uvf5k.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = MongoClient(URI)
db = client[DB]
pprint.pprint(db[COLLECTION].find_one())
client.close()
```

![](https://i.imgur.com/Wgs8Gjb.png)

***

**Reference:**
- [Day13 — 架起MongoDB囉!](https://ithelp.ithome.com.tw/articles/10236244?sc=iThelpR)