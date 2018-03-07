---
layout: post
title: "[Tutorial]Computer Networking筆記(22-26)"
date: 2018-01-25 20:29
author: "Shihs"
category: Tutorial
---

[Computer Networking Tutorial](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBpuvPW0aHa7mKdn_k9SPKO)

## **How Binary Code Works?**
- bit = binary digit
- 8-bit system 最高到2^8

舉例，如果今天我們要表示19這個數字，那就會是<br>
2^8、2^7、2^6、2^5、2^4、2^3、2^2、2^1、2^0<br>
 0 、 0 、 0 、 0 、 1 、 0 、 0 、 1 、 1<br>
 
在8 bits的系統裡，可以表示從0到255的數字。<br>
也就是，111111111<br>

所以如果今天有更多的bits就可以儲存更多的data，
這也就是為什麼更大的bits功能較強大了。



## **IP Address**
每個device都有ip address。

IP是一個32 bits的2進位表示的數字，<br>
中間以「.」隔開成四組號碼。<br>
像這樣:xxx.xxx.xxx.xxx<br>
每一組xxx都是8-bit，也就是一個八位數的0、1所組成的數字，<br>
所以，每一組有2^8(256)個數字，總共就會有2^8*2^8*2^8*2^組IP。<br>
而我們看到的IP則是再把這些2進位的數字轉換成10進位表示。<br>

這樣的方式就可以讓每個device表達它的位置。



## **IP Addressing Issues**
The Internet is a network of networks.

影片舉了一個例子：
想像網路其實是聚集了所有的網絡。
例如，社區網路是一個網絡，學校是一個網絡，公司是一個網絡，
而這三個網絡又都可以連到網路上。

當今天，公司裡有台電腦送了requests到網路另一端的server，
這時候server收到訊息後，會再傳回response，
可是它要如何透過IP知道到底找到這個送出requests的裝置呢？

所以其實IP裡頭包含兩個訊息，
1. Newwork ID
2. Host ID

但是，重點來了！<br>
那一組32 bits的IP要怎麼表示Newwork ID和Host ID呢？<br>
如果對分，讓16 bits表示Newwork ID，16 bits表示Host ID，<br>
這樣就可以有65,536個Newwork ID配上Host ID的組合。<br>
但這時候有人說，那萬一某個network的host很少，<br>
那豈不是浪費了很多host的位址嗎！<br>
但讓host多點bits或少點bits都有可能會遇到浪費或是不夠的問題，<br>
這時候大家有點爭論不休，<br>
到底該如何解決呢？<br>

所以這時有人提出了一個辦法，<br>
我們應該要用一個方法表示出Network ID和Host ID的長度。<br>

[*Subnet mask(子網路遮罩)*](https://www.youtube.com/watch?v=D0a9hTEW48Y)<br>
當今天在傳送訊息時，<br>
device不只傳送自己的ip，也傳送subnet mask來表示network id和host id長度，<br>

subnet mask一樣是一個32 bits的2進位數字，<br>
1表示network id，0表示host id。<br>
[(這裡看影片應該會比較好理解)](https://www.youtube.com/watch?v=FM169QUIQco&list=PL6gx4Cwl9DGBpuvPW0aHa7mKdn_k9SPKO&index=25)<br>
[詳細範例](https://www.youtube.com/watch?v=Upk5MU7vGAg&index=26&list=PL6gx4Cwl9DGBpuvPW0aHa7mKdn_k9SPKO)<br>


