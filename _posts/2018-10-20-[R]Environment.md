---
layout: post
comments: true
title: "[R]Environments (1)"
date: 2018-10-20 15:26
author: "Shihs"
category: [R]
---

這篇要介紹 R 的環境(Environments)。

我個人覺得環境是一個寫程式很重要但一開始會很困惑的東西，之前一直處於似懂非懂的狀態。
<br>
其實如果只是用 R 來跑一些數據分析，其實不理解環境並不會造成什麼太大的問題，但如果能夠懂當然絕對是有利無弊。
<br>
最近有了寫 R package 的經驗後，讓我開始對「環境」比較了解，所以這篇想要將我的理解記錄下來。

***

### 1. 什麼是環境（Environments）？

當我們每次打開 R studio 這時候便是打開了某個環境，接著我們產生了一些變數，這些變數便是在這個環境底下。

很抽象嗎？
<br>
打開 R studio 時，在右上的框框（或是在某個位置）有個「Environment」，然後可以看到如下圖的「Gloabal Environment」，並且在下面的框框可以看到我們產生的變數（圖中的 x）。
![enrionment variable.png]({{ "/img/posts/enrionment variable.png" | absolute_url }}){:height="395px" width="380px"}


這就表示，我們現在在「Gloabal Environment」這個環境底下，且 x 這個變數在「Gloabal Environment」環境中。

當我們把「Gloabal Environment」這個圖往下拉，可以看到像下圖這樣（每個人的可能都不太一樣）
![enrionment.png]({{ "/img/posts/enrionment.png" | absolute_url }}){:height="395px" width="380px"}
依序往下就會是「Gloabal Environment」的 「parent 環境」。

（「parent 環境」是殺毀？！）

**環境就像是房間**

我覺得可以把「環境」想像是一個房間。
<br>
當妳/你在操作 R ，產生任何變數，做任何動作，都是在這個房間裡面操作（通常一打開 R studio 都會是在 Global 環境）。所以這些變數全部都會被放在這個房間裡。或是想像在一個房間裡縫娃娃這些娃娃做完都會被放在這個房間裡。

那「parent 環境」就會是，妳/你走出這個房間來到客廳，也就是說，這個房間是被包在家裡的，走出家裡，整個家是被包在建築物裡的，然後社區，然後某條路，某個區，某個縣市......就是一個俄羅斯娃娃的感覺。往上一層就會是「parent 環境」、「grand parent 環境」.....以此類推。

***

### 2. R 是如何在環境裡找變數的？

根據上面的解釋我們知道，每次操作 R 的時候我們都會是在某個環境底下。
<br>
那這和 R 要找變數有什麼關係呢？

在這之前我們先來看我現在有幾間房間呢？
```r
search()
# [1] ".GlobalEnv"        "tools:rstudio"     "package:stats"     "package:graphics"  "package:grDevices"
# [6] "package:utils"     "package:datasets"  "package:methods"   "Autoloads"         "package:base"
```
這表示，最底下的環境是`.GlobalEnv`(Gloabal Environment)，它的 parent 變數是`tools:rstudio`，再往上是`package:stats`......等等，最後會是`package:base`，但其實最上層會是 Empty environment。

**在房間裡找東西？**

如果今天妳/你人在一個房間裡找東西妳/你會怎麼找？
<br>
一定會先在房間裡搜尋一遍，如果怎麼都找不到，就會去客廳找，再找不到就到這棟建築物找......一直往外找對吧？

所以同樣的，如果今天我們想要找個變數 x，結果 R 發現找不到，那它就會往 parent 環境（search()的順序）找，再找不到就會再往上找，如果一直找到最上層還是沒有，就會跳出像這樣的錯誤。
```r
x
# Error: object 'x' not found
```
找的方式就像是這個圖，[source](http://adv-r.had.co.nz/Environments.html)
![search path.png]({{ "/img/posts/search path.png" | absolute_url }}){:height="160px" width="500px"}


**parent 是誰？**

我們可以用`parent.env()`來查看上一層環境，
```r
now.env <- environment()
parent.env <- parent.env(now.env)
grandparent.env <- parent.env(parent.env)
```

***

### 3. 可以增加環境嗎？
如果仔細看剛剛`search()`的結果會發現，那些都是 package 呢！
<br>
其實在每次使用 `library()`或是`require()` attache 一個 pacakge 後環境就會被改變，這時 Gloabal Environment 的 parent 環境就會變成這個 package。（請自行實驗）

***

（題外話）
<br>
**library() v.s require()**
這兩者到底有什麼差別呢？

基本上兩個的差別只有在於找不到這個 package 時，`library()` 會產生 Error 暫停程式，`require()`會 FALSE 並吐出 Warning ，然後繼續執行程式。
<br>
所以可以把`require()`包在 if 裡，如果沒有這個 package 就安裝，程式也能繼續執行。

```r
> library(x)
# Error in library(x) : there is no package called ‘x’

require(x)
# Loading required package: x
# Warning message:
# In library(package, lib.loc = lib.loc, character.only = TRUE, logical.return = TRUE,  :
#  there is no package called ‘x’
```
（題外話結束）

***

也就是說，如果我們今天使用`library()`或是`require()`就會讓環境改變。
<br>
所以如果今天是要 create package 的話，千萬不要將 `library()`和`require()`包在任何 function，這樣非常危險，可能會造成 [Namespace](http://r-pkgs.had.co.nz/namespace.html) 的混亂。（如果看不懂可以先忽略這段）

那如果今天需要用到這個包，但是又不想讓它加到 search path（parent 環境）裡怎麼辦？

這時候請使用`::`。例如，今天想要呼叫 pkg1 裡頭的 fun()，
```r
pkg1::fun()
```
`::`還有一個很好用的時刻，就是當今天有兩個不同的 package 擁有兩個同樣名稱的 function 時，先載入的 package 順序會被放在後面，所以如果直接呼叫 funciton ，一定會用到後載入的 package 的 function。

如果現在是 pkg1 和 pkg2 都有 fun()，那我們可以這樣用，
```r
# 呼叫 pkg1 的 fun
pkg1::fun()

# 呼叫 pkg2 的 fun
pkg2::fun()
```
這樣就絕對不會出錯了。
不過記得，要使用`::`必須要有 install 這個 package 才能使用。

**Attaching v.s Loading**

library() 和 require() 這兩個 function 的動作都是 **Attaching**，也就是會將這 package 加到 parent 環境 (search path)。
<br>
但 `::`則是 **Loading**，也就是說，這個 pacakge 在 loading 後可以在記憶體（memory）中被找到，但不會被加到 parent 環境 (search path) 中。
[source](http://r-pkgs.had.co.nz/namespace.html#search-path)

***

下次介紹
<br>
1. `new.env()`和 function 中的環境
2. <- 和 <<- 的差別


***

Reference:
<br>
[Advance R - Environments](http://adv-r.had.co.nz/Environments.html)
<br>
[R package - Namespace](http://r-pkgs.had.co.nz/namespace.html)
<br>
[Build a R package for yourself](https://www.gl-li.com/2017/09/14/build-a-r-package-for-yourself/)
<br>
[Making Your First R Package](http://tinyheero.github.io/jekyll/update/2015/07/26/making-your-first-R-package.html)
