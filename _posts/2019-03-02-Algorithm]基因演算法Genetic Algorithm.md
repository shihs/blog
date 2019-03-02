---
layout: post
comments: true
title: "[Algorithm]基因演算法Genetic Algorithm"
date: 2019-03-02 15:58
author: "Shihs"
category: [Algorithm]
---

基因演算法（Genetic Algorithm）是一種求函數極值的最佳化（函數的最大或最小值）的方法。

它的想法是來自於基因遺傳，透過細胞分裂將好的基因保留，不好的基因淘汰，一代傳一代，最後留下最適合生存的物種，所謂「適者生存」。
實現的方式就像基因的機制那樣，透過*隨機*選擇後，再進行 crossover 和 mutation，經過多次迭代後，最後結果將會收斂到一個最佳解。但這最佳解不ㄧ定是 global maximum（minimum），通常是 local maximum（minimum）。

（但其實這與基因的真實行為完全無關，就像是 Neural Network 和人類神經反應的真實行為無關一樣。）

***
### 演算法流程圖
![genetic algorithm.gif]({{ "/img/posts/genetic algorithm.gif" | absolute_url }}){:height="380px" width="600px"}
[Source](https://dotblogs.com.tw/dragon229/2013/01/03/86692)

1. 一開始隨機產生n個變數 (n由使用者決定)
2. 利用適應函數（fitness function）計算所有變數的適應值
3. 依每個的適應值進行「選擇、複製」
4. 對留下的變數進行交配（crossover）及突變（mutation）的動作

***

### 範例 

以下範例是來自[演算法筆記的 Optimization](http://www.csie.ntnu.edu.tw/~u91029/Optimization.html)


1.
[初始化]
一開始先隨便弄出幾個x。本例是四個。

	1010101010
	1011001011
	1110101011
	0010101000

2.
[fitness function]
根據問題特性，定義好壞程度。

	f(1010101010) = 678

3.
[selection]
隨便找個位置切一刀，每個x都被分成兩段。

	1010101  010
	1011001  011
	1110101  011
	0010101  000

4.
[crossover]
隨便找兩組你覺得夠優良的x，交叉相接變成新答案。
重複一直做，直到x數目跟原先一樣多。本例是四個。

	1010101 \/ 010  ->  1010101 -- 011
	1011001 /\ 011      1011001 -- 010 


	1010101011
	1011001010
	1110101010
	1010101000

5.
[mutation]
每個x都隨便找一個地方把數字改掉，也可以不改。

	1010111011
	1011001000
	1110101010
	1010101001

6.
重複3. 4. 5.，直到裡面有一個x是你滿意的，令f(x)最大的那個x。
1. 隨機產生N個x。
2. 計算fitness function。
3. 重複以下步驟，直到有一個x讓人滿意。
<br>
　甲、selection。
<br>
　乙、crossover。
<br>
　丙、mutation。
<br>
　丁、計算fitness function。


一開始的 x 的足夠豐富，多演化幾次就可以得到不錯的結果。一開始的 x 足夠豐富，可以避免進入區域極值。 mutation 用於增加 x 的豐富性，以跳脫區域極值。

***

Reference:

[演算法筆記 - Optimization](http://www.csie.ntnu.edu.tw/~u91029/Optimization.html)
<br>
[Genetic Algorithm 基因演算法](http://littledoa.wixsite.com/pcclab/single-post/2016/02/03/Genetic-Algorithm-基因演算法)
<br>
[人工智慧系列之基因演算法](https://www.youtube.com/watch?v=UE6YkRWBtZk)
