---
layout: post
comments: true
title: "[Neural Network]Convolution Neural Network 卷積神經網路"
date: 2020-02-01 10:45
author: "Shihs"
category: [Machine Learning, Neural Network]
---

之前寫了兩篇的 CNN 課程筆記，但後來因為太忙沒有繼續看完課程就中斷了 T_T。
<br>
[[Machine Learning]Covolutional Neural Networks(CNN)(1)](https://shihs.github.io/blog/machine%20learning/2019/02/25/Machine-Learning-Covolutional-Neural-Networks(CNN)/)
<br>
[[Machine Learning]Covolutional Neural Networks(CNN)(2)](https://shihs.github.io/blog/machine%20learning/2019/03/02/Machine-Learning-Covolutional-Neural-Networks(CNN)(2)/)

卷積神經網絡(Convolutional Neural Network)簡稱 CNN，主要應用在影像辨識，這篇想要簡單的說明 CNN 的概念。

***

先看下面兩張 CNN 概念圖

[圖片來源](https://www.kdnuggets.com/2016/11/intuitive-explanation-convolutional-neural-networks.html/3)
![]({{ "/img/posts/CNN 概念圖 1.png" |absolute_url}})


[圖片來源](https://medium.com/jameslearningnote/資料分析-機器學習-第5-1講-卷積神經網絡介紹-convolutional-neural-network-4f8249d65d4f)
![]({{ "/img/posts/CNN 概念圖 2.png" |absolute_url}})

從上圖可以看到整個流程各經過兩次的 Convolution、Pooling 和 Fully Connected，所以其實只要搞懂 **Convolution**、**Pooling** 和 **Fully Connected** 分別在做什麼就可以掌握 CNN 了。

整個流程是，前面的 Convolution 和 Pooling (又稱為 subsampling) 在做的是 feature extraction (特徵擷取)，而 Fully connection 在做的是 classification (分類辨識)。

***

## 1. Convolution Layer 卷積層

Convolution Layer 包括 filter 和激活函數 (ex. Relu) 所構成。

下圖是常見的美圖效果，其實就是使用 filter 達成的
[圖片來源](https://medium.com/雞雞與兔兔的工程世界/機器學習-ml-note-convolution-neural-network-卷積神經網路-bfa8566744e9)
![]({{ "/img/posts/美圖.png" |absolute_url}})

卷積 (Convolution) 做的是特徵擷取，而不同的效果在做的就是對不同的特徵做擷取。例如，銳化效果在做的就是強化邊緣的特徵，也就是加強擷取出邊緣的特徵。

那所以卷積到底是如何擷取不同的特徵的呢？
[圖片來源](https://icecreamlabs.com/2018/08/19/3x3-convolution-filters%E2%80%8A-%E2%80%8Aa-popular-choice/)

![]({{ "/img/posts/Convolution.gif" |absolute_url}})

特徵擷取的方式是使用 Filter (或稱作 Kernel) 來萃取圖片中的特徵，上圖是一個 3x3 window 的 filter，而算法就是像圖那樣移動 (移動的步數是 stride)，將數字相乘後再相加 (詳情可以看之前的[筆記1](https://shihs.github.io/blog/machine%20learning/2019/02/25/Machine-Learning-Covolutional-Neural-Networks(CNN)/)、[筆記2](https://shihs.github.io/blog/machine%20learning/2019/03/02/Machine-Learning-Covolutional-Neural-Networks(CNN)(2)/)，包括 padding 和 stride 的概念)。美圖的不同效果就是使用不同的 Filter (Kernel) 做出來的。

下圖是不同的 filter 做出來的效果
[圖片來源](https://icecreamlabs.com/2018/08/19/3x3-convolution-filters%E2%80%8A-%E2%80%8Aa-popular-choice/)

![]({{ "/img/posts/kernels.png" |absolute_url}})

現在明白了 filter，但再回去看最一開始的流程圖，為什麼 converlution 有三個呢？這是因為使用了三個 filter 去擷取不同的特徵。


看完 filter 再看 Relu。可以看到最上圖圖中有個 Relu，也就是將所有計算出來結果的負值都變為 0。
[圖片來源](https://medium.com/jameslearningnote/資料分析-機器學習-第5-1講-卷積神經網絡介紹-convolutional-neural-network-4f8249d65d4f)

![]({{ "/img/posts/Relu.png" |absolute_url}})


如果是彩色的圖，通常會有三個 channel (RGB)，也就是一開始輸入的 image 有三個，可以看下圖
[圖片來源](https://zhuanlan.zhihu.com/p/42559190)

![]({{ "/img/posts/three images convolution.jpg" |absolute_url}})

## 2. Pooling Layer 池化層

pooling 又稱為 subsampling，是為了提取特定區域主要特徵，但又想要減少參數的數量，以防止模型過擬合，常用的是 max pooling，也就是取該區域最大的值，也有 average pooling，也就是取該區域的平均值。
[圖片來源](https://zhuanlan.zhihu.com/p/42559190)

下圖是取 max pooling，使用 2x2 的 window，且 stride 為 2

![]({{ "/img/posts/pooling.jpg" |absolute_url}})


## 3. Fully Connected Layer 全連接層

Fully Connected Layer 主要是進行 Flattening 平坦化，將最後的矩陣轉換成一維，然後再使用傳統的 neural network + softmax()。


參考我之前的[[Neural Network]Neural Network 1](https://shihs.github.io/blog/neural%20network/2020/01/22/Neural-Network-Neural-Network/)


***

以上就是 CNN 的流程。

最後提一下，從上面的過程我們可以知道，CNN 整個過程中需要求解的參數是

1. Convolution layer filters
2. Full Connected Layer filters

[來源](http://doremi2016.logdown.com/posts/2017/01/25/convolutional-neural-networks-cnn)


***

**Reference:**
<br>
[[資料分析&機器學習] 第5.1講: 卷積神經網絡介紹(Convolutional Neural Network)
](https://medium.com/jameslearningnote/資料分析-機器學習-第5-1講-卷積神經網絡介紹-convolutional-neural-network-4f8249d65d4f)
<br>
[[機器學習 ML NOTE]Convolution Neural Network 卷積神經網路](https://medium.com/雞雞與兔兔的工程世界/機器學習-ml-note-convolution-neural-network-卷積神經網路-bfa8566744e9)
<br>
[【DL笔记6】从此明白了卷积神经网络（CNN）](https://zhuanlan.zhihu.com/p/42559190)
<br>
[Convolutional Neural Networks' (CNN) Backward Propagation](http://doremi2016.logdown.com/posts/2017/01/25/convolutional-neural-networks-cnn)