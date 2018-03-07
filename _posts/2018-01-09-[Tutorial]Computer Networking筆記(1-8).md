---
layout: post
title: "[Tutorial]Computer Networking筆記(1-8)"
date: 2018-01-09 15:27
author: "Shihs"
category: Tutorial
---

[Computer Networking Tutorial](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBpuvPW0aHa7mKdn_k9SPKO)

## **1.What is Computer Networking?**
各裝置(*devices*)之間的連結<br>
裝置：PC、laptop、printer、rounter等等(不限於電腦)，每一個device都是一個***Node***。<br>
連結：可以使用cable、wireless、copper wire等等，可以稱為***communications media***。<br>
Internet(網路)就是一種computer network<br>

computer nework的目的是為了要資料傳輸、資料交換，<br>
這裡的資料可以是，documents、pictures、videos等等。

computer newworking的兩個重點就是，***Nodes***和***Communications Media***


## **2.Types of Networks**
***LAN***(Local Area Network)：一個building的網絡連結，可能是一棟建築、一所學校，小範圍的區域網絡<br>
***MAN***(Metorpolitan Area Network)：多個建築之間的網絡連結，可能是一個城市<br>
***WAN***(Wide Area Network)：>30 miles的網絡連結，整個國家之間、跨國之間的連結<br>


## **3.How the Internet works?**
以網站為例，假如我今天有一個個人網站，別人是如何透過internet看到我的網站的呢？<br>
如果以上面computer network的邏輯來看，<br>
其他電腦可以連結到我的電腦，看到我的個人網站。<br>
但，如果所有人都可以連到我的個人電腦這樣會有網路安全的疑慮，<br>
所以實際上，要連到個人網站是透過***server***。<br>
server is a special computer that everyone can access it.<br>

我將個人網站建置(store)在server，<br>
其他人要看到我的網站，<br>
會在browser上打上網址，<br>
這時候就會向server提出request，<br>
sever接受到request會回傳data，這些data會是程式碼，<br>
而browser會將這些程式碼轉成我們看得懂的網站。<br>

通常建置網頁這樣的server我們稱為，***web server***。<br>
像google這麼大的網站，一次總是要接收非常大量來自世界各地的request，<br>
所以這個server就必須要有很大的memory，<br>
才能負荷這樣的使用流量。<br>

## **4.Client and Host**
根據上面提到的例子，<br>
使用PC的browser向sever提出request，<br>
然後server會提供給data給PC的browser。<br>

PC接收資料，而server提供資料，<br>
PC就是client，sever就是host。<br>



