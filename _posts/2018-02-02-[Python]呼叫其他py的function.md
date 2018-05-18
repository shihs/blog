---
layout: post
comments: true
title: "[Python]呼叫其他.py的function"
date: 2018-02-02 16:56
author: "Shihs"
category: Python
---
假如現在正在寫的檔案是main.py，而你想要呼叫fun.py這裡面的function，
要怎麼做呢？

```python
### 這是fun.py
def itsafunction():
	print "This is a function that I want to call."

```


有兩種情況，<br>
**1. 這兩個檔案在同一個folder底下**<br>
---main.py<br>
---fun.py<br>
      
```python
### 這是 main.py
from fun import itsafunction

# 使用fun.py的itsafunction()
itsafunction()

```

**2. 這兩個檔案在不同folder底下**<br>
想要呼叫的fun.py在function這個folder底下<br>
---main.py<br>
---function---fun.py<br>

這時候main.py可以有兩種寫法
```python
### 這是main1.py
from function import fun

# 使用fun.py的itsafunction()
fun.itsafunction()
```


```python
### 這是main2.py
from function.fun import itsafunction

# 使用fun.py的itsafunction()
itsafunction()
```

但還有一件很重要的事，要**在function這個folder裡加"\_\_init\_\_.py"這個檔案**
```python
### 這是__init___.py
# 什麼都不用寫，沒錯，就是一個空白的.py檔
# it's true, it's empty. But it's still important!
```

那如果今天fun.py在function的下一層folder呢?<br>
---main.py<br>
---function---another---fun.py<br>
只要把main.py改成<br>

```python
### 這是main.py
from function.another import fun

# 使用fun.py的itsafunction()
fun.itsafunction()

#或者也可以這樣寫

from function.another.fun import itsafunction

# 使用fun.py的itsafunction()
itsafunction()
```
但最重要的是，<br>
**function和another這兩個folder裡面都要加上"\_\_init\_\_.py"這個檔案!**



