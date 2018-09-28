---
layout: post
comments: true
title: "[R]scale 與 dist function"
date: 2018-09-27 18:04
author: "Shihs"
category: [R]
---

這篇文章會介紹 R 中的 scale 與 dist 兩個 function。

在做資料分析前會需要先標準化


***

### scale
scale 的主要作用在標準化數據，共有三個 arguments，
- x: 必須要是 matrix，以「行」為每組數據計算
- center: TRUE or FALSE。中心化，TRUE 會減去數據的平均值
- scale: TRUE or FALSE。 TRUE 會將數據中的每個值除以數據的標準差

預設 center 和 scale 都是 TRUE，也就是算出來的值是 [z-score](https://zh.wikipedia.org/wiki/標準分數)。

>
\\(z = \frac{x - \mu}{\sigma}, \sigma \neq 0\\)

其中：<br>
\\(x\\)：數據<br>
\\(\mu\\)：平均值<br>
\\(\sigma\\)：標準差


```r
x <- matrix(1:10, nrow = 5)

scale(x)
```

***

### dist
dist 是在算數據間的距離，主要的 arguments有
- x: 可以是 matrix, data.frame ，但必須要是 numeric。
- methods: 共有六種計算距離的方法，"euclidean", "maximum", "manhattan", "canberra", "binary" 和 "minkowski"，預設是使用 euclidean 距離。

以「列」為數據，兩兩計算，

```r
x <- matrix(1:10, nrow = 5)

dist(x)
```








