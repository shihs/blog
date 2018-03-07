---
layout: post
title: "[Python]Read and Write CSV file"
date: 2018-01-08 11:32
author: "Shihs"
category: Python
---

```python
import csv

# read csv file
with open("file.csv", "rb") as f:
    for row in csv.reader(f):
        print row
    



# write csv file
data = [["data1", "data2"], ["data3", "data4"]]  # list 
with open("file.csv", "wb") as f:
    w = csv.writer(f)
    w.writerows(data)

```