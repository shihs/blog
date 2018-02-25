---
layout: post
title: "[[Tutorial]Computer Networking筆記(9-11)"
date: 2018-01-15 22:40
author: "Shihs"
---

[Computer Newworking筆記](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBpuvPW0aHa7mKdn_k9SPKO)

## **1.What is NIC(Network Interface Card)?**
NIC就是網卡，所有電腦都必須要有網卡才能連上網路。<br>
(just google it, you can find tons of pictures of NIC)

## **2.What is a Protocol?**
字典翻譯的意思是，協議草案、禮儀。<br>
在network裡，protocol是「網路傳輸協定」。

這裡作者先不講定義，先講一個communication會有什麼要件，<br>
他用男生想要認識一個女生來舉例。

一開始男生要搭訕女生他們可能會有像這樣的對話
-                    Hey  ->
-                         <-  Hello
- Can I get your number?   -> 
-                         <- 1234-567

這樣的對話中會有幾個規則，
1. 一次只會有一個人說話
2. 男生說話以後，會預期女生會回話
3. 問句會有預期的回答(specific messages receive specific responses)<br>
符合這樣的規則，那麼人之間的對話(communication)才會有可能成立。

同樣的，用在computer commnication也要有一些規則。<br>
Protocol are the rules for successful communication among two parties.

如果今天你的mac想要和web sever communicates這時候protocol會是什麼呢？
- Can I connect to you?   ->
- <-   Yes, you have my permission.
- GET file google.com   ->
- <-  sends file

在computer networking裡，最重要的protocol是<br>
**format**和**order** of massage<br>
就像是上面的請求順序，<br>
如果在mac還沒提出request，<br>
sever就送出網頁，這肯定很怪的吧！<br>

protocol有很多種，
但我們先來看以下這個例子。<br>
這是個網址，<br>
http:// www.thenewboston.org /index.php

- **http**: protocol
- **www.thenewboston.org**: sever name
- **index.php**: file




