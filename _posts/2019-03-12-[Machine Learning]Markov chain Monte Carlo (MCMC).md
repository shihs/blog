---
layout: post
comments: true
title: "[Machine Learning]Markov Chain Monte Carlo (MCMC)"
date: 2019-03-12 14:58
author: "Shihs"
category: [Machine Learning]
---

**MCMC 是什麼？**

Markov Chain Monte Carlo （MCMC）是一種抽樣方法，用來解決無法直接抽樣的分佈的隨機抽樣問題。

**The Goal of MCMC**

We want to sample from some distribution p, or approximate an $$E[f(x)] ~ where ~ (X \sim p)$$
<br>
通常 p 是一個很複雜的 distribution，要從這個分佈取 sample 根本不可能，所以這時候就會需要 MCMC。

***

**為什麼要使用 MCMC？**

在 Baysian Inference 中常使用到這個公式

$$p(\theta\mid y) = \frac{p(y \mid \theta) p(\theta)}{\int p(y \mid \theta) p(\theta)d\theta}$$

或是，它的參數 $$\theta$$ 的貝式估計

$$\hat \theta = E[\theta \mid y] = \int \theta p(y \mid \theta) d \theta = \frac{\int \theta p(y \mid \theta) p(\theta)}{\int p(y \mid \theta) p(\theta)d\theta}$$

其中的 $$p(\theta)$$ 為先驗機率 (prior probability)，基本上我們無法獲得 $$p(\theta)$$ 的值，這時候就需要 MCMC。

***

MCMC 由兩部分的觀念 (步驟) 組成, 一個是 「Markov Chain」 ，另一個則是「Monte Carlo integration」，接下來將說明這兩個部分。

***

**Monte Carlo Integration**

Monte Carlo Integration 可以以抽樣平均的方式計算上面的期望值式子

$$E[\theta \mid y] \approx \frac{1}{n}\sum_{i=1}^{t}{(\theta_i \mid y)}, ~ \theta_i \stackrel{iid}{\sim} p(\theta \mid y)$$

也就是說，使用樣本平均數來估計期望值。這件事情可以成立是因為，根據大數法則，當樣本數 n 夠大時，樣本的平均數將趨近於母體平均數。

這樣看起來 Monte Carlo Integration 讓我們省去了上面那個看起來複雜的積分式子。但是，現實生活中很多時候並無法從 $$p(\theta \mid y)$$ 這個 distribution 抽樣，要不就是不知道這個 distribution，要不就是這個 distribution 爆炸複雜啊。

所以說，哪有這麼好的事？

這時候可以採用其他的抽樣方法，譬如，*rejection sampling*, *importance sampling* 和本文的重點 *MCMC*。

***

**Markov Chain**

- Markov Chain (馬可夫鍊)：A Markov chain is a sequence $$X_0, X_1, ...$$ of random variables such that the distribution of the next value depends only on the current on (and parameters). 現在有一隨機變數數列 $$X_0, X_1, ...$$，且每一個變數只和前一個變數有關，也就是 $$X_{t+1}$$ 來自 $$p(X_{t+1} \mid X_t)$$，像這樣的數列我們就稱為馬可夫鍊。

- $$p(X_{t+1} \mid X_t)$$ 被稱為這個馬可夫鍊的轉換核心 (transition kernel)

- A Markov chain is stationary, with stationary distribution $$Φ, if ~\forall k ~ X_k  \sim Φ$$

- One shows (not trivial in general) that under *certain* conditions a Markov chain will converge to the stationary distribution in the limit. 在一般條件假設底下，馬可夫鍊的變數分配將收斂到目標機率函數 $$\pi(·)$$ 並且與 $$X_0$$ 的選擇無關。


*Monte Carlo Integration*可以看[這裡](https://www.youtube.com/watch?v=MKnjsqYVG4Y)



***

Reference:
<br>
[(ML 18.1) Markov chain Monte Carlo (MCMC) introduction-12eZWG0Z5gY.mp4](https://www.youtube.com/watch?v=3ZmW_7NXVvk)
<br>
[The Markov Chain Monte Carlo Simulations](http://web.ntpu.edu.tw/~ccw/statmath/M_mcmc.pdf)
<br> 
Linköping University - 732A90 Computational Statistics 2019 Lecture 4 slide
<br>
[[数据分析] Markov Chain Monte Carlo](https://zhuanlan.zhihu.com/p/25610149)
<br>
[徐亦达机器学习课程 Markov Chain Monte Carlo](https://www.youtube.com/watch?v=s8w8AsFK77c&list=PLyAft-JyjIYq2SLTHO2ptmx-cChbE5GBm)
<br>
[MCMC(一)蒙特卡罗方法](http://www.cnblogs.com/pinard/p/6625739.html)
