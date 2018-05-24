---
layout: post
comments: true
title: "[Tutorial]Computer Networking筆記(12-15)"
date: 2018-01-20 16:26
author: "Shihs"
category: Tutorial
---

[Computer Networking Tutorial](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBpuvPW0aHa7mKdn_k9SPKO){:target="_blank"}

## **Topology/Layout**
[Topology/Layout](https://zh.wikipedia.org/wiki/网络拓扑){:target="_blank"}是網路之間連接的方式，wiki上翻成「網路拓樸」。<br>
每一種方式都各有有缺點，所以取決於使用的目的來決定適合哪種Layout。

這個課程介紹三種方式：
1. Bus Topology(Tutorial 12)
2. Ring Topology(Tutorial 13)
3. Star Topology(Tutorial 14)



**1. Bus Topology**<br>
[Bus Topology](https://zh.wikipedia.org/wiki/匯流排拓撲){:target="_blank"}是最簡單的一種連接方式，最主要中間有一條主幹，<br>
其他node再與主幹相連。最重要的是，主幹的尾端一定要有terminator，<br>
才能將傳到尾端的訊號吸收，否則會有回傳的訊號干擾。<br>

這樣的優點就是，簡單而且便宜，<br>
適合使用在小範圍的網絡內。<br>

但缺點是，只有主幹上出了問題，整個網路可能就會出問題。<br>


**2. Ring Topology**<br>
[Ring Topology](https://zh.wikipedia.org/wiki/環狀拓撲){:target="_blank"}與Bus Topology不同的是，它是一個沒有終端環狀，<br>
所有node與該環狀線連結，訊號會順著同一個方向傳遞。<br>
一般來說，會有兩個環狀(double ring)，訊號會是反方向傳遞。<br>

這樣的優點就是，它不需要Bus Topology必須的terminator，<br>
而且如果是雙環，也比較不會有主幹出問題，<br>
整個網路就壞掉的問題。<br>

但缺點是，<br>
它比Bus Topology貴。<br>


**3. Star Topology**<br>
[Star Topology](https://zh.wikipedia.org/wiki/星型网){:target="_blank"}可能是家裡最常見的一種連結方式。<br>
Star Topology會有許多nodes連結中的device(譬如rounter)，就像是星狀一樣。<br>
例如，如果中心是rounter，它會在連結internet。<br>

這種topology的優點是，價格低、easy to expand。<br>
另一方面，如果有其中的node或是某一個node與中心的device的連結出了問題，其他nodes都不會被影響。<br>

但缺點是，因為所有nodes都連結中心，<br>
也就是所有的nodes全部都必須要依賴中心，<br>
所以只要中心的device壞掉，整個連線就會全部失效。<br>


**4.Mesh Topology**<br>
[Mesh Topology](https://zh.wikipedia.org/wiki/网状网络){:target="_blank"}所有nodes之間都互相連結，就像個網狀。<br>
這種方式比較會在MAN或WAN見到，不會在LAN使用。<br>

優點是，因為每個node之間都互相連結，<br>
所以假如有兩個nodes之間的連結出了問題，<br>
還可以透過其他nodes傳遞訊號，<br>
這樣在傳送訊息上也比較保險。<br>

缺點是，因為每個node之間都要連接，就會需要有很多的cable，<br>
這時候成本就會提高。有越多的node，成本就會越高。<br>
另一方面，因為一個node需要和其他所有nodes連結，<br>
這時候網卡(NIC)就需要更強大，同樣也會造成成本的提高，<br>
且每一次增加node可能都需要增加NIC。<br>


