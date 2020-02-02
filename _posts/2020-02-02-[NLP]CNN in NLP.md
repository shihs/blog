---
layout: post
comments: true
title: "[NLP]CNN in NLP"
date: 2020-02-02 10:35
author: "Shihs"
category: [NLP, Machine Learning, Neural Network]
---

[前一篇](https://shihs.github.io/blog/machine%20learning/neural%20network/2020/02/01/Machine-Learning-Convolution-Neural-N卷積神經網路/)介紹了 CNN 的概念，這篇要來介紹 CNN 如何運用在 NLP 中。

***

Yoon Kim 在 2014 年發表論文 [Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882) 提出將 CNN 運用在 NLP。

![]({{ "/img/posts/CNN in NLP.png" |absolute_url}})

上圖就是 Yoon Kim 論文提出的方法概念，和在圖像運用的 CNN 一樣，有 convolution 和 pooling，然後最後是一個 softmax function。

我們先來看第一步，

## Convolution

在圖片中，我們將圖片看成一個 nxm 的矩陣，每一格都是一個數字，而我們可以使用 filter(kernel) 來獲取想要的特徵。而在 NLP 中，如果想要將文字表示成數字，可以使用 word embedding，例如 word2vect、glove，或是 one-hot encode 的詞彙到索引詞向量表示方法。

上圖中的第一個矩陣是 'I love this movie very much!' 的 word embedding 矩陣，每一列代表一個 word 的向量。總共有七個字，每一個字用一個 5 維的向量表示，所以用一個 7x5 的矩陣表示。



**filter**

現在知道了輸入的表示法，那在 convolution 中最重要的 filter 要如何使用呢？

一般 CNN 的 filter 會是一個方正矩陣，從左往右再往下滑動，但在 NLP 中，filter 矩陣會和向量的維度一樣，但一次可能滑動兩個字 (2-grams)、三個字 (3-grams)等等，這個稱作 region size，看上圖的第二大行，有紅色系、綠色系、黃色系三種 filter，分別代表 region size 4、3 和 2，且各有兩個，也就是總共有六個 filter。(像這樣移動的方式只有一個方向叫做，[1D converlution](https://blog.goodaudience.com/introduction-to-1d-convolutional-neural-networks-in-keras-for-time-sequences-3a7ff801a2cf))

整張大圖的第三行，就是輸入矩陣 (channel) 乘上 filter 之後的結果。


## Pooling

Convolution 的下一步是 pooling，上圖使用的是 max pooling，也就是取最大的值。

pooling 後 flatten 所有值，最後一步 softmax function 便完成了。





***

**Reference:**
<br>
[Simple Deep Neural Networks for Text Classification](https://www.youtube.com/watch?v=wNBaNhvL4pg)
<br>
[Understanding Convolutional Neural Networks for NLP
](https://kiseliu.github.io/2016/09/22/understanding-convolutional-neural-networks-for-nlp/)
<br>
[Introduction to 1D Convolutional Neural Networks in Keras for Time Sequences](https://blog.goodaudience.com/introduction-to-1d-convolutional-neural-networks-in-keras-for-time-sequences-3a7ff801a2cf)