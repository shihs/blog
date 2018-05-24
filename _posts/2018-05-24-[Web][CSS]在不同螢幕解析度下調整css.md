---
layout: post
comments: true
title: "[Web][CSS]在不同螢幕解析度下調整css"
date: 2018-05-24 14:47
author: "Shihs"
category: [Web, CSS]
---


除了電腦外手機、平板都可以瀏覽網頁，這篇要介紹如何依據不同裝置的螢幕寬度來調整 CSS。

[參考網站](http://www.ucamc.com/e-learning/css/102-rwd-css-media-type.html)

## 解析度可以這樣區分
1. 手機：解析度為0px~320px<br>
2. 平板電腦：解析度為320px~768px<br>
3. 桌上型電腦：大於768px<br>

<br>

## 在 CSS 上調整

使用*@media*

**設定 Max Width**
```css
/* 768px以下(包含)都適用，手機和平板會符合這個設定 */
@media (max-width 768px) {
	.class {
		background: #ccc;
	}
}
```

**設定 Min Width**
```css
/* 329px以上(包含)都適用，平板和電腦會符合這個設定 */
@media (min-width 320px) {
	.class {
		background: #666;
	}
}
```

**設定 Max Width and Min Width**
```css
/* 介於768px與979px間適用 */
@media (min-width: 768px) and (max-width: 979px) {
	.class {
		background: #666;
	}
}
```


如此就可以依據螢幕的寬度來顯示適合的方式了。






