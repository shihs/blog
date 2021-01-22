---
layout: post
comments: true
title: "[Python]asyncio 和 await"
date: 2021-01-22 19:26
author: "Shihs"
category: [Python]
---






```python
import requests
import time
import asyncio

url = 'https://www.google.com.tw/'
loop = asyncio.get_event_loop()

start_time = time.time()

async def send_req(url):
    t = time.time()
    print("Send a request at",t-start_time,"seconds.")

    res = await loop.run_in_executor(None,requests.get,url)

    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")

tasks = []

for i in range(10):
    task = loop.create_task(send_req(url))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
```

***

**Reference:**
<br>
[python的asyncio模組(一)：異步執行的好處](https://ithelp.ithome.com.tw/articles/10199385)
<br>
