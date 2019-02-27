---
layout: post
comments: true
title: "[Python]filter、map、reduce、lambda"
date: 2019-02-27 12:02
author: "Shihs"
category: [Python]
---

- lambda 可以直接定義一些簡單的 funciton。
- filter、map和reduce這三個函數有點像 R 裡頭的 apply 家族系列。

***

**lambda**

我其實覺得就是定義 funciton，只是是定義一些簡單，可以一行完成的 funciton。
```python
# 回傳輸入的變數 + 1
fun = lambda x: x + 1
print (fun(3))
# 上面的 func 其實就等於
def fun(x):
  return x+1


# 輸入兩個變數
fun = lambda x, y: x+y
print (fun(3, 5))


# 含 if
fun = lambda x: True if x % 2 == 0 else False
print (fun(3))
```
***

**filter(function, sequence)**

對 sequence 中的 item 依序執行 function(item)，然後將執行結果為 True 的 item 組成一個 list/string/tuple（與 sequence 類型相同）回傳。
這時候 function 可以使用 lambda 定義或是平常的 def 定義。

```python
# 回傳是數字，除 0 外都是 True
fun = lambda x: x-1
print (filter(fun, range(3)))

# function 為 def
def f(x): return x % 2 != 0 and x % 3 != 0 
print (filter(f, range(2, 25)) )

# function 為 lambda
f = lambda x: x % 2 != 0 and x % 3 != 0 
print (filter(f, range(2, 25)) )

```
***

**map(function, sequence)** 

對 sequence 中的 item 依序執行 function(item)，執行結果以 list 回傳。

```python
# funciton 只有一個參數
res = map(lambda x: x**2, range(1, 11))
print (res)
# 每次都回傳 1
res = map(lambda i: 1, range(1, 11))
print (res)


# function 有兩個參數
res = map(lambda x, y: x*y, range(1, 11), range(2, 12))
print (res)
```
***

**reduce(function, sequence, starting_value)**

對 sequence 中的 item 順序迭代調用 function，最後回傳一個值。

```python
from functools import reduce # 在 python3 是必須的

# 求 list 的和
res = reduce(lambda x, y: x+y, range(1, 10))
print (res)
```


***
Reference:
<br>
[Python特殊语法：filter、map、reduce、lambda [转]](https://www.cnblogs.com/longdouhzt/archive/2012/05/19/2508844.html)