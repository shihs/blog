---
layout: post
comments: true
title: "[Python][SQL]Python 連接 SQLite"
date: 2018-06-30 13:01
author: "Shihs"
category: [Python, SQL]
---

這篇是 Python 連接 SQL 的一些基本語法，<br>
內容來自 Udacity 上 [Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197) 的免費課程與我自己整理的資訊。


```python
import sqlite3

conn = sqlite3.connect("Cookies") # 連接 SQLite 資料庫
cursor = conn.cursor() # 獲得連接的游標

# 要下的 SQL 指令
cursor.execute(
    "select host_key from cookies limit 10;"
)

results = cursor.fetchall()

print resutls # 結果為 turple

conn.close() # 每次都要記得 close 連線
```