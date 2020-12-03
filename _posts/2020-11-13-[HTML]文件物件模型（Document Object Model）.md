---
layout: post
comments: true
title: "[HTML]文件物件模型（Document Object Model）"
date: 2020-11-13 15:36
author: "Shihs"
category: [HTML]
---

### DOM 是什麼？

DOM 是 Document Object Model（文件物件模型）的縮寫，它是 HTML、XML 和 SVG 文件的程式介面（programming interface）；可以理解成 DOM 是文件和程式溝通的橋樑、介面，也可以說，DOM 是針對 HTML、XML 和 SVG 提供的一個 API，為了讓程式（ex. JavaScript）能夠操作文件的內容。DOM 將文件（HTML、XML 和 SVG）用樹狀結構表示（如下圖），樹中的每一個節點（node）皆為物件（object），DOM 定義了一些方法讓程式可以存取這些的節點（node）/ 物件（object）並改變文件架構、風格（CSS）和內容。


**[Treehouse 的課程](https://teamtreehouse.com/library/what-is-the-dom)這樣解釋：**
- The DOM is a represenation (map) of a webpage that JavaScript can use. 
- The DOM represents a web page as a tree-like structure.


另外，寫網頁的時候常使用 JavaScript 來存取 DOM，但 DOM 並不屬於 JavaScript 語言的一部分，只是我們常用 JavaScript 去存取 DOM，換句話說，JavaScript 可以用其他語言取代，只是不常見。


|![DOM tree.png]({{ "/img/posts/DOM tree.png" |absolute_url}})|
|:--:| 
| [The DOM represents a web page as a tree-like structure](https://teamtreehouse.com/library/what-is-the-dom) |


|![]({{ "/img/posts/DOM.gif" |absolute_url}})|
|:--:| 
| [Example of DOM hierarchy in an HTML document](https://ithelp.ithome.com.tw/articles/10202689) |

***

### 為什麼需要 DOM？

為的是要讓不同的瀏覽器有一樣的文件物件模型標準，否則我們現在就都得針對不同的瀏覽器個別寫程式碼了。而這個標準是由 [W3C](https://zh.wikipedia.org/wiki/%E4%B8%87%E7%BB%B4%E7%BD%91%E8%81%94%E7%9B%9F)（全球資訊網協會）所定義的。

***

### DOM 解析

DOM 的樹狀結構中最重要的就是**節點**（**node**），而節點可以分為下列四種（以 HTML 為例，看上圖）：

- **Document**：Document 就是指這整份文件，就是這份 HTML 檔的開端，所有的 nodes 都會從 Document 開始往下。

- **Element**：Element 是指文件內的各個標籤，像是 `<html>`、`<body>`、`<div>`、`<p>` 等等各種 HTML Tag 都被歸類在 Element。

- **Attribute**：Attribute 是指各個標籤內的相關屬性，像是 `name`、`class`、`href` 等等都是被歸類在 Attribute。

- **Text**：Text 是指被各個標籤包起來的文字，像是 `<h1>Hi</h1>` 中， Hi 被 `<h1>` 這個 Element 包起來，因此 Hi 就是此 Element 的 Text。

***

### API = DOM + JavaScript

這邊介紹一些常見的 DOM API，

```javascript
document.body;
document.getElementById('idName');
document.getElementsByTagName('tagName');
document.getElementsByClassName('className');

// selector 可以是 id:#idName, class:.className, tag:tagName, or CSS pseudo-class
document.querySelector('selector'); 
document.querySelectorAll('selector');
```

***

### 補充：BOM & window

**BOM** 是 Browser Object Model（瀏覽器物件模型）的縮寫。DOM 是文件和程式溝通的接口，BOM 則是和瀏覽器溝通的接口。像是跳轉到其他頁面、螢幕大小的參數等等可以操作的方法或屬性。

同樣的 BOM 也有很多屬於它的 object，像是 `location`，下面這個程式碼可以讓瀏覽器跳轉到另一個頁面：

```javascript
location.href = "http://www.xxxx.com";
```

而 **windows** 也是 **BOM** 的一個 object。「關閉視窗」可以這樣寫，

```javascript
window.close();
```



***

**Reference:**
<br>
[Day03-深入理解網頁架構：DOM](https://ithelp.ithome.com.tw/articles/10202689)
<br>
[W3C DOM](https://www.wibibi.com/info.php?tid=379)
<br>
[文件物件模型 (DOM)](https://developer.mozilla.org/zh-TW/docs/Web/API/Document_Object_Model)
<br>
[JavaScript DOM (Document Object Model)](https://www.fooish.com/javascript/dom/)
<br>
[DOM, DOCUMENT, BOM, WINDOW 有什么区别?](https://www.zhihu.com/question/33453164)



