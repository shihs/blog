---
layout: post
comments: true
title: "[R]RStudtio編碼問題"
date: 2018-10-04 23:42
author: "Shihs"
category: [R]
---

解決編碼問題可以說最惱人的事了......<br>
在使用中文或是其他歐語系語言時經常碰到編碼問題，這篇我根據我自己的一些經驗整理了一些在使用 RStudio 時解決編碼問題的辦法。

***

根據我的經驗，我覺得編碼問題可以分成三種，
1. R 程式碼編碼問題
2. 檔案編碼問題
3. 系統編碼問題




### 1. R 程式碼編碼問題
當你打開一份 R Script 時，發現 script 中的中文都是亂碼時，這時應該是這份 script 檔案的編碼與你電腦的 RScript 預設的不同。

這時選擇 File -> Reopen with Encoding... 更改編碼(UTF-8、BIG5、ASCII試試)，問題應該就可以解決了。

或是可以直接更改預設的讀檔編碼，到 Tools -> Global Options... -> (左邊選單) Code -> Saving 更改 Default text encoding。


### 2. 檔案編碼問題
當你讀進一份檔案，可能碰到以下幾種狀況<br>

a. 讀檔時出現編碼錯誤<br>
解決方法： <br>
(1)讀檔時設定 fileEncoding：讀檔時提供檔案本身編碼資訊，[參考](https://shihs.github.io/blog/r/2018/01/17/R-read.csv出現編碼錯誤訊息/)<br>


(2)更改檔案編碼：先更改檔案本身的編碼，再使用 RStudio 讀取檔案。<br>
   如果是 Windows，我個人推薦直接使用記事本更改最方便。另存新檔直接存成需要的編碼。<br>

(3)更改預設讀檔編碼：如第一個提到的 R 程式碼編碼問題的解決方案，直接更改預設的編碼，設定成 UTF-8 應該是最好的。<br>


b. 順利讀進檔案，但無法正確顯示<br>
讀檔時，使用 encoding 參數來決定要顯示什麼語言

```r
read.csv("filename.csv", encoding = "latin1")
```



### 3. 系統編碼問題
順利讀進檔案，已更改輸入時的編碼，但顯示仍舊錯誤。<br>
這問題是在讀一份含有瑞典文的檔案時碰到的，已經更改過檔案的編碼，但開啟後仍無法正確顯示瑞典文。

可以檢查一下系統本身的編碼是不是 UTF-8 
```r
sessionInfo() # 裡的 local
# 或是
Sys.getlocale()

# MAC 會長得大概像這樣
# "en_US.UTF-8/en_US.UTF-8/en_US.UTF-8/C/en_US.UTF-8/en_US.UTF-8"
```
如果不是，更改系統的語系，以下更改為 UTF-8
```r
# for windows
Sys.setlocale(category = "LC_ALL", locale = "UTF-8")

# for mac
Sys.setlocale(category = "LC_ALL", locale = "en_US.UTF-8")
```

***

另外，要查看 vector 的編碼可以使用
```r
# x is a vector
Encoding(x)
```


我個人認為，解決編碼問題最重要的就是要先知道編碼出錯的問題在哪。<br>
是檔案本身編碼問題，還是系統的問題，那是要修改檔案還是要修改系統？<br>













