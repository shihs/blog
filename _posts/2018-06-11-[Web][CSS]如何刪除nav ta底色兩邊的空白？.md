---
layout: post
comments: true
title: "[Web][CSS]如何刪除 nav tag 底色兩邊的空白？"
date: 2018-06-11 14:51
author: "Shihs"
category: [Web, CSS]
---


###  `<nav>`的作用

1. `<nav>` 為 HTML 文件的區域元素 (element)，`<nav>`用來規劃網頁的導覽區域，通常裡頭會放網站其他網頁的連結。
2. `<nav>` 除了全域屬性外，沒有定義其他屬性 (attribute) 。
[參考](https://pydoing.blogspot.com/2012/01/html-5-nav.html)

像我的[網頁](https://shihs.github.io/)上面黑色那條有 "About" 和 "Contact Me" 連結的區域就是在 `<nav>`裡。

<br>

```html
<!-- html -->
<body>
  <nav class="wrapper-nav" id="nav">
    <ul>
      <li><a href="#about">About</a></li>    
      <li><a href="#contact">Contact Me</a></li>
    </ul>           
  </nav>
</body>
```

```css
/* css */
nav {
  background-color: black;
}
```

<br>

### 如何刪除 `<nav>` 背景的空白 How to remove the space on both sides of navbar
若使用上面的程式碼會發現 `nav` 底色變成黑色，但兩邊會有無法移除的空白，這時候有兩種解決方法。皆是在`<body>`這個 tag 上面做些調整

1. 
```css
/* css */
body{
  margin-left:auto;
  margin-right:auto;
} 
```

2. 
```css
/* css */
body{
  width: 100%;
  margin: auto;
} 
```






