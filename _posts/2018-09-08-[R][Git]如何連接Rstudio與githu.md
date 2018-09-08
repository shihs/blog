---
layout: post
comments: true
title: "[R][Git]如何在 Rstudio 上連接 R project 與 Github"
date: 2018-09-08 10:53
author: "Shihs"
category: [R, Git]
---

本篇介紹如何將 Rstudio 中的 R project 與 Github 連結，讓每次專案在進行中都可以簡單快速的 commit 與 push。

在進入主題前，請先安裝好 R、Rstudio 和 Git ，並且申請好 Github 帳號。


***


## 前置作業 ##
**設置 SSH RSA key**

1.複製 public key
Tool > Global Options > Git/SVN > Create RSA Key > View public key <br>
點開 View public key 後，複製裡頭所有的東西。

![Rstudio SSH.png]({{ "/img/posts/Rstudio SSH.png" | absolute_url }})



2.將 public key 貼到 github 

![github ssh.png]({{ "/img/posts/github ssh.png" | absolute_url }}) 


***


## 開始建立 connection ##

**建立專案**

請先建立一個專案，這裡就不多加解釋了。


**在本機建立 repository**

Build > Configure public Tools > Git/SVN
將 Version control system 由 None 改為 Git

![version control system.png]({{ "/img/posts/version control system.png" | absolute_url }}) 

這時候就會發現 Rstudio 的視窗長得不太一樣了。

![rstudio git.png]({{ "/img/posts/rstudio git.png" | absolute_url }}) 

下方視窗應該會有一些還未 commit 的檔案，但因為我都已經 commit 了，所以沒有內容。<br>
且這時候 pull 和 push 鍵應該還無法操作。


**Github 同步**

終於來到最後一哩路。

到 Github 上創建一個新的 repository，且名稱要和 project 相同，只要單純創建 repository 就好，什麼檔案都不要。

最後，打開 Rstudio 工具列的， Tools > Shell

然後在 Shell 裡輸入，
``` git
git remote add origin https://github.com/你的github帳號/你的專案名稱.git
git push -u origin master
```

完成後就會發現專案已經和 Github 連結了！專案的檔案都出現在 Github 上了。<br>
這時候 pull 和 push 鍵也已經可以操作了。



未來只要更新專案內容，就可以直接在 Rstudio 上 commit 和 push 就好了！


***

**補充**

移除 project 與該 repository 的 connection `rm -rf .git`






***
參考：

* Hadley Wickham 的 [R Package Git 章節](http://r-pkgs.had.co.nz/git.html) 

