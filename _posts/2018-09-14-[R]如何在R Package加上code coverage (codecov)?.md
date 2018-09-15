---
layout: post
comments: true
title: "[R]如何在R Package加上code coverage (codecov)?"
date: 2018-09-14 18:04
author: "Shihs"
category: [R]
---

[code coverage](https://zh.wikipedia.org/wiki/代碼覆蓋率)(代碼覆蓋率)?

這篇是根據[這篇](https://walczak.org/2017/06/how-to-add-code-coverage-codecov-to-your-r-package/)的步驟操作。
如果要找 package 內容物該有的東西可以參考我完成的一個 [R package](https://github.com/shihs/LiUAdRLab3)。

以下會將步驟一一列下。

***

### 1. 完成 R package 與建立 test 測試
建立 [R package](http://r-pkgs.had.co.nz) 可以參考大神的書，test 則可以參考這本書的 [testing 章節](http://r-pkgs.had.co.nz/tests.html)。

基本上使用，
```r
devtools::use_testthat()
```
就會自己建立一個 [tests 資料夾](https://github.com/shihs/LiUAdRLab3/tree/master/tests)，再把要測試的程式碼加進下一層的 [testthat 資料夾](https://github.com/shihs/LiUAdRLab3/tree/master/tests/testthat)內。

最後進行測試，
```r
devtools::test()
```

***

### 2. 建立所有 code coverage 需要的檔案與內容

先跑一下程式碼，
```r
devtools::use_coverage()
```

跑完後會出現以下的步驟提示，

```
* Creating `codecov.yml` from template.
* Adding `codecov.yml` to `.Rbuildignore`.
* Add to `README.md`: 
[![Coverage Status](https://img.shields.io/codecov/c/github/shihs/LiUAdRLab3/master.svg)](https://codecov.io/github/shihs/LiUAdRLab3?branch=master)
* Add to `.travis.yml`:
after_success:
  - Rscript -e 'covr::codecov()'
```

基本上就一步一步照著做就對了，前面兩件事程式已經幫你處理好了，<br>
從第三步開始就行。


### 3. 將 Github 與 codecov 連結

使用 Github 帳號登入 [codecov.io ](https://codecov.io)。

連結你要使用 codecov 的 reposity，
會出現像這樣的[畫面](https://walczak.org/wp-content/uploads/2017/06/token.png)得到一組 token，
將 token 複製，在 R 中跑以下程式碼，


```r
install.packages("covr")
library(covr)
codecov(token = "YOUR_TOKEN_GOES_HERE")
```

大功告成！


這時候會看到你剛剛貼上的 coverage 圖案出現 code coverage 的結果。

***

如果想要先在 R studio 上看測試結果可以使用，

```r
library (covr)
report()
```

viewer 視窗就會顯示測試結果了。




