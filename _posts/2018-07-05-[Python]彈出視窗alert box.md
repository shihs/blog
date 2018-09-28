---
layout: post
comments: true
title: "[Python]彈出視窗 alert box"
date: 2018-07-05 15:39
author: "Shihs"
category: [Python]
---

介紹如何使用 python 寫彈跳視窗，其實網路上可以找到蠻多方法的，我這邊就簡單介紹幾個。<br>
以下會分為 mac 和 windows 兩個系統來討論。


## Mac ##

### 1. easygui 套件 ###
```python
# 記得先安裝 easygui 套件
from easygui import msgbox
msgbox('Stuff')
```
這個套件基本上蠻簡單的，只要使用`msgbox()`就好，<br>
如果只是要在跑程式的時候使用沒有太大問題，<br>

更多 [easygui 套件](https://blog.csdn.net/marksinoberg/article/details/51499909) 的介紹

但如果要把程式碼打包時（[pyinstaller套件](https://shihs.github.io/blog/python/2018/05/24/Python-使用pyinstaller套件打包.py檔/)） 這個方法就會失效，會出現錯誤訊息
```
ImportError: No module named easygui
[3310] Failed to execute script alterwindow
```
所以如果要讓程式碼打包後可以出現彈跳視窗可以使用內建的 system。

### 2. os.system() ###
```python
import os

os.system("osascript -e 'Tell application \"System Events\" to display dialog \""+"Some Funky Message"+"\"'")
```
這方法其實就是使用 python 執行**系統命令**。
也就是，其實把 os.system() 括號裡的東西
```
osascript -e 'Tell application "System Events" to display dialog "Some Funky Message"'
```
打在 terminal 裡會執行的東西。

將以上命令打在 terminal 會發現出現一個彈跳視窗，內容是 Some Funcky Message。
![system_msg.jpg]({{ "/img/posts/system_msg.jpg" | absolute_url }})

所以在 python 裡面同樣執行會產生同樣的結果。

而這個方法將程式打包後可以正確執行。
<br>
<br>

## Windows ##
### 1. easygui 套件 ###
```python
# 記得先安裝 easygui 套件
from easygui import msgbox
msgbox('Stuff')
```
基本上和 mac 一樣，將程式碼打包後也無法正常執行。


### 2. ctypes 套件 ###

```python
# 不需另外安裝
import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

# 或著你可以定義一個 function
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxA(0, text, title, style)
Mbox('Your title', 'Your text', 1)

# 如果是要輸出中文，記得重新 encode
ctypes.windll.user32.MessageBoxA(0, "內容".decode("utf-8").encode("big5"), "標題".decode("utf-8").encode("big5"), 1)
```
這個方法也可以打包後執行。

另外，
會看到有些地方使用
```
ctypes.windll.user32.MessageBoxW()
```
而不是
```
ctypes.windll.user32.MessageBoxA()
```
但執行後會發現，`ctypes.windll.user32.MessageBoxW()`這個方法會出現亂碼。

這兩個的差別在`MessageBoxW`要使用 unicode 編碼，而`MessageBoxA`是 ascii 編碼。<br>
[有人回答](https://stackoverflow.com/questions/20783046/python-program-displaying-messages-in-different-language-than-english)這個問題	。

這邊 mac 和 windows 各介紹了兩種方法，其實還有很多方法啦，只要能符合需求的都是好方法！







