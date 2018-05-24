---
layout: post
comments: true
title: "[Python]下載與安裝 Python2.7 及 pip 套件"
date: 2018-05-23 15:25
author: "Shihs"
category: [Python]
---

安裝前可以先認識 [Python](https://zh.wikipedia.org/wiki/Python){:target="_blank"}。


這篇文章將會介紹如何在 windows 系統中下載與安裝 python2.7 以及安裝 pip 套件。

主要步驟其實就是四個：
1. 下載Python
2. 設定環境變數
3. 下載get-pip.py
4. 設定環境變數


### 1.下載 Python2.7

[Python2.7.14載點](https://www.python.org/downloads/release/python-2714/)
根據自己電腦是32位元還是64位元選擇要下載的檔案
![python downloads.jpg]({{ "/img/posts/python downloads.jpg" | absolute_url }})

下載下來後的檔案（我的電腦是32位元）
![python installation.jpg]({{ "/img/posts/python installation.jpg" | absolute_url }})

點兩下安裝，就是一直按下一步就對了
![python install step.jpg]({{ "/img/posts/python install step.jpg" | absolute_url }})





### 2.設定環境變數
設定環境變數的目的是，在執行 Python 時讓系統可以根據環境變數底下的路徑依序去找 Python 程式，而不會不知道要如何執行 Python。

設定環境變數步驟，<br>

電腦(右鍵)->內容
![environment.jpg]({{ "/img/posts/environment.jpg" | absolute_url }})

1.進階系統設定 -> 2.環境變數 -> 3.點選PATH->編輯
![environment variable.jpg]({{ "/img/posts/environment variable.jpg" | absolute_url }})

在變數最後加上安裝路徑「;C:\Python27」（這是預設的安裝路徑，如果安裝過程中有更改位置，這邊要改成安裝的路徑）
![python path.jpg]({{ "/img/posts/python path.jpg" | absolute_url }})



以上步驟完成之後在 cmd 輸入 python，就開始執行 Python 了！ 
![python test.jpg]({{ "/img/posts/python test.jpg" | absolute_url }})



<br>
基本上到這裡已經安裝好 Python 了，那為什麼要安裝 pip 呢？<br>

Python 有很多別人寫好且非常好用的套件，當我們想要使用這些套件前會需要先下載安裝套件，而 pip 是用來下載其他套件非常好用的工具。<br>

當我們下載完 pip 後，
未來下載套件只需要在 cmd 輸入指令就能搞定。
```
pip install packagename
```

也許現在還是會有點困惑，但未來真正開始寫 Python 就會明白為什麼大家下載完 Python 都會接著安裝 pip 了。


### 3.下載 get-pip.py
先下載 [get-pip.py]({{ "/downloads/get-pip.py" | absolute_url }})

接著開啟 cmd，使用 cd 將目前位置移到 get-pip.py 的路徑底下，並輸入
```
python get-pip.py
```
![run pip_get.jpg]({{ "/img/posts/run pip_get.jpg" | absolute_url }})


這時候只差最後一步了



### 4.設定環境變數
這個步驟與剛剛第2個步驟一樣，不過現在要加上的路徑是「;C:\Python27\Script」
![python script path.jpg]({{ "/img/posts/python script path.jpg" | absolute_url }})

<br>
<br>
接著使用 pip install 安裝看看套件，例如可以安裝寫爬蟲程式必備的 requests 套件
```
pip install requests
```
如果沒有問題，一切就大功告成！<br>




