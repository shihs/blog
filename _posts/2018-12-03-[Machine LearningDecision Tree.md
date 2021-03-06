---
layout: post
comments: true
title: "[Machine Learning]Random Forest"
date: 2018-12-03 14:07
author: "Shihs"
category: [Machine Learning]
---

基本上 Random Frost 是要改善 Decision Tree 容易 overfitting 的問題，它結合了 Decision Tree 和 bagging 的方法。

Random Forest 是建立很多顆決策樹，再利用多數決選出最好的選項，和 [bagging](https://shihs.github.io/blog/machine%20learning/2018/12/03/Machine-Learning-Bagging/) 這篇提到的方法有點類似，但有些小差異。

使用的方法是 bagging（結合多個 model），所以這也是 Ensemble learning。

***

**Random Forest步驟**

假如有一 training data，有 N 個樣本，p 個features。
<br>
今天要利用這個 training data 建立一個 Random Forest model，裡頭共有 B 棵決策樹，

1. 使用 boostrap 從 training data 中抽出 N 個樣本產生一組 data
2. 在這組 data 中隨機從 p 個 featrues 中選取 m (m < p) 個 features，再從這 m 個 features 找出最好的一個分割結果，如此產生一個 node
3. 重複步驟 2，直到完成這個 model 為止
4. 重複步驟 1~3 B 次，共會產生 B 棵擁有不同 feature 的決策樹

最後要進行 predict 時，分類問題使用多數決，回歸問題使用平均數決定。

***

- 因為每一棵樹的隨機選取的樣本與 feature 都不同，所以每棵樹的結果都不會相同。
- Random Frost 建立的 decision tree 不需要 pruning。在 decision tree 剪枝是爲了避免 overfitting，但在 Random Frost 使用 bagging 的方式就已經避免 overfitting 了。
- 因為每一棵決策樹都是隨機篩選 feature 的結果，所以可以想像每棵樹就像是精通某個領域的專家。當有個新的數據近來，經由各個領域的專家投票表決，做出最後的選擇。
- Random Forest 中有兩個參數需要人為控制，一個是樹的數量（B），一般建議取很大。另一個是 feature 的大小（m）。

- 優點：
1. 不用做特徵（feature）選擇。
2. 訓練完後可以知道哪些 feature 比較重要。

***

Reference:
<br>
[StatQuest: Random Forests Part 1 - Building, Using and Evaluating](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)
<br>
[随机森林（Random Forest）算法原理](https://blog.csdn.net/edogawachia/article/details/79357844)
<br>
[AdaBoost和随机森林的区别](https://blog.csdn.net/niuniuyuh/article/details/54346930)