---
layout: post
comments: true
title: "字元編碼，ASCII、Unicode、UTF-8"
date: 2019-01-22 16:38
author: "Shihs"
category: [Others]
---

關於編碼，相信大家很常聽到 ASCII、Unicode、UTF-8 這幾個名詞，這篇要根據我的理解來介紹這三個名詞。若有錯歡迎指正:)
<br>
2022/03/15 上完 Harvard CS50 的 Lecture 0 後做了一些新增與修改。


***

## 字元編碼

- 在電腦的世界是使用二進位（binary）的方式來進行運算，也就是 0 與 1 兩個 digits（each binary digit called bit）。
- 而電腦是使用「關」與「開」來表示二進位中的 0 與 1。
- 在現代電腦中是由上百萬的電晶體（transistors）來控制這樣的「關」與「開」（0 與 1）。


***

## ASCII
[ASCII](https://zh.wikipedia.org/wiki/ASCII) 是電腦早期發展時由美國制定的一套編碼規則，且沿用至今。它的目的是用來統一規範，規定數字與字母大小寫、符號等等的對應關係，而每一個數字由 8 個 bits 表示。最後一次更新是在1986年，至今為止共定義了 128 個字元。

像是 `HI!` 就是由數字 72、73 和 33 所組成的。由二進位表示就是，`01001000`、`01001001`、`00100001`。


**Extended ASCII**
<br>
但因為一個 byte 共有 8 個 bits，也就是說還有很多個位元並未使用到，所以後來又產生了 Extended ASCII。很多歐洲國家有一些字母並未在 ASCII 中，所以除了 ASCII 為固定的字元外，每個國家根據自己所需給與字元，但也造成每個國家並未統一編碼。（[Wikipedia](https://zh.wikipedia.org/zh-tw/EASCII)）

***

## Unicode
隨著網際網路的發展，世界各國交換訊息，未統一的編碼便造成了很大的問題。這時候有了 Unicode 的誕生。

Unicode 協會將所有的文字與符號都分配一個數字，這個數字的寫起來像是，U+0645，而這個數字就稱為 Code point。U+ 的意思是 Unicode，
數字則是用十六進位表示。

但 Unicode 編碼使用至少兩個位元儲存字元，若是今天只有英文，仍舊是每個字元使用兩個位元儲存，這表示浪費了很多的資源。所以這時候有有人想出了更好的辦法。

***

## UTF-8
有人發明了 UTF-8 這種儲存方式。

UTF-8 編碼把一個 Unicode 字元根據不同的數字大小編碼成 1-6 個字節，常用的英文本母被編碼成 1 個字節，漢字通常是 3 個字節。如果今天要傳輸的內容都是英文，這時使用 UTF-8 編碼就能省下空間。


**比較**
<br>
Unicode 是一種編碼方式，和 ASCII 是同一個概念，而 UTF-8 是一種存儲方式，在存儲和傳輸上節約空間、提高性能的一種編碼形式

***

Reference:
<br>
[字符编码笔记：ASCII，Unicode 和 UTF-8](http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html)
<br>
[淺談電腦編碼與 Unicode (一) 基礎概念篇](http://blog.chunnorris.cc/2015/04/unicode.html)
<br>
[常見三種字符編碼的區別：ASCII、Unicode、UTF-8](https://hk.saowen.com/a/6615242f89d424bc28e35ea8efc115707b2ec7dcf43bb52491bca9805f99a118)
<br>
[[轉錄] [doc] 每個軟體開發者都絕對一定要會的Unicode及字元集必備知](https://www.pttweb.cc/bbs/ISU_CSIE94B/M.1152573430.A.88F)
<br>
[CS50 2022 - Lecture 0](https://cs50.harvard.edu/x/2022/notes/0/)
