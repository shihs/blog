---
layout: post
comments: true
title: "[Python]使用 pyinstaller 套件打包 .py 檔"
date: 2018-05-24 11:05
author: "Shihs"
category: [Python]
---

當我們今天寫好一個 .py 檔，要給使用者執行時當然可以幫使用這在他們的電腦下載 Python 等執行檔案時需要的套件，但是，**很麻煩！！！** <br>

不可能每次有一個新的使用者就要重新安裝一次 Python，還要安裝套件(更不要說有時候安裝套件會碰到一些問題)，且要執行 .py 檔對於不會使用 terminal 或是 cmd 的人來說可能會乾脆放棄，這也減少了讓妳/你的程式給更多人使用的機會。<br>

而 **pyinstaller** 是一個可以把 .py 打包成一個 .exe 檔的工具，讓使用者只要點兩下就能執行妳/你寫好的 Python 檔案。<br>
<br>

## 前提
pyinstaller可以在 Windows、MacOS、Linux 上使用，但是不是跨平台，所以如果今天使用者是 windows 那麼就必須要在 windows 作業系統底下產生 .exe 檔，若使用者是 macOS 那就必須要在 mac 底下打包產生執行檔。<br>



## 安裝
**Windows**
```
pip install pyinstaller
```


**Mac**
```
sudo pip install pyinstaller
```
但我這邊在安裝時出現了一大串的錯誤，但內容包括 
*[Errno 1] Operation not permitted*

後來我參考[這裡](https://blog.csdn.net/helloxiaozhe/article/details/78603183)把指令改成
```
sudo pip install pyinstaller --upgrade --ignore-installed
```
就成功安裝了。<br>
安裝好後，可以在 cmd 或是 terminal 上輸入 pyinstaller 確認。<br>




## 打包 .py 檔
假如現在要打包一個 test.py 檔
**Windows**
```
pyinstall -F test.py
```
完成後會產生三個檔案，
1. build 資料夾
2. dist 資料夾
3. test.spec 檔

而我們需要的 test.exe 會單獨在 dist 資料夾裡，如果要給其他 Windows 使用者執行 test.py 這支檔案，只需要給他們 .exe 就行了。<br>
如果 test.py 這支程式是會產生一個檔案，例如 .csv 檔案，則這檔案會直接儲存在和 test.exe 同一個路徑底下。


**Mac**<br>
Mac的操作基本上和 Windows 指令一樣，
```
pyinstall -F test.py
```
打包完後產生出來的檔案也會一樣。<br>
但如果執行 .exe 檔會產生檔案，這時候會發現檔案沒有出現在和 .exe 同一個路徑底下。而是會在 /Users/*yourusername* 底下。<br>
<br>
可以試試看在 .py 檔裡增加一行 
```
print os.getcwd()
``` 
會發現使用 .exe 執行的結果就會是 /Users/*yourusername*，所以檔案才會直接產生在這路徑底下。<br>

但我想要讓檔案直接產生在桌面，因此我的方法是加上這行 
```
os.chdir('/Users/'+os.getlogin()+'/Desktop')
```
讓路徑直接換到桌面，這樣儲存檔案就會產生在桌面上了。<br>








## 常用參數
1. pyinstaller -h 查看參數
2. -F 打包成一個exe文件
3. –icon=圖標路徑





<br>
關於 pyinstaller 套件，這個[部落格](http://legendtkl.com/2015/11/06/pyinstaller/)我覺得說明蠻詳細的。















