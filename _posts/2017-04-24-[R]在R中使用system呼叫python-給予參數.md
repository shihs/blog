---
layout: post
comments: true
title: "[R]在R中使用system呼叫python-給予參數"
date: 2017-04-24 11:22
author: "Shihs"
category: R
---

之前介紹過[在R中使用system呼叫python](https://shihs.github.io/blog/2016/07/08/R-在R中使用system呼叫python/)。
```R
system("python python_script.py")
```

假如現在我想要帶入參數給python script要怎麼做呢？

首先，<br>
在python程式碼的部分，<br>
要使用 **sys.arg[]** 讓python程式獲取參數。

還有，在 **sys.arg[0]** 表示的是程式名稱，<br>
所以要使用 **sys.arg[1]** 才是表示要讀取的第一個參數。

假如今天有支 *python_script.py*
```python
# -*- coding: utf-8 -*-
import sys

string = "Hello, " + sys.argv[1]
print string
```

在cmf中呼叫這支python程式
```
python python_script.py world
```

R裡的system()要打的指令就是cmf中打的指令。<br>
所以在R中就會變成，<br>

```R
system("python python_script.py world")
```
結果就會變成
```
Hello, world
```

最後，<br>
在使用system()必須要先setwd將路徑設成python_script.py所在位置。


