---
layout: post
comments: true
title: "[Machine Learning]Covolutional Neural Networks(CNN)(1)"
date: 2019-02-25 16:29
author: "Shihs"
category: [Machine Learning]
---

這篇為 Coursera 上 [Convolutional Neural Networks](https://www.coursera.org/learn/convolutional-neural-networks/home/welcome) 這門課第一週的 Computer Vision、Edge Detection Example 和 More Edge Detection 筆記。

***

**前言：**

因為 Deep Learning 的快速發展，所以電腦視覺（computer vision）這幾年也迅速的超展開。像是自動駕駛就受惠於 computer vision 的進步，讓自駕車不會撞到路人和其他車輛；或是人臉辨識系統也變得更厲害，像是手機的人臉辨識解鎖；或是使用 Deep Learning 辨別照片是屬於風景照、人、動物還是車輛等等（像是 iphone 的相簿現在就很變態的會自動歸類照片是什麼）；甚至在藝術上都有 Deep Learning 的蹤影。

***

**為什麼要使用 Covolutional Neural Networks(CNN)？**

**Computer Vision Problem**

![Computer Vision Problem.png]({{ "/img/posts/Computer Vision Problem.png" | absolute_url }}){:height="400px" width="600px"}

以上圖的例子來看，第一張是 64x64 的照片，第二張畫素則是 1000x1000，這時候如果再加上 RGB 三原色的維度，兩張照片的維度分別會是 64x64x3 和 1000x1000x3。以 Neural Network 來實作的話（右下角），input layer 的 Xn 的 n = 1000x1000x3，如果第一層的 hidden 是 1000 個 nodes，這時候轉換的 W 的維度就會是 1000x3000000，這是不是很 CRAZY？

所以這時候就會碰到以下的問題。

**缺點**
1. 很難避免 overfitting
2. 計算上需要大量的電腦效能和 CPU，實在太不切實際了

因此，為了解決的這個問題，我們就需要用到 CNN。

***

**CNN 的流程圖** [Sourse](https://res.mdpi.com/entropy/entropy-19-00242/article_deploy/html/images/entropy-19-00242-g001.png)
![CNN.png]({{ "/img/posts/CNN.png" | absolute_url }}){:height="300px" width="630px"}

***

**How the convolution operation works?**

現在先來看 convolutional layer 的部分，也是 CNN 非常重要的一個環節。這邊使用 Edge detection 作為範例操作 convolution operation 是如何運作的。

**Edge detection example**

![edge detect.png]({{ "/img/posts/edge detect.png" | absolute_url }}){:height="400px" width="600px"}

在辨識下圖時我們可能會想要做垂直的邊緣辨識和水平的邊緣辨識。那要如何操作呢？

**Vertical edge detection**

![convolutional operation.png]({{ "/img/posts/convolutional operation.png" | absolute_url }}){:height="400px" width="600px"}

最左邊的圖是一張 6x6 pixel 的黑白圖，每個 pixel 的數字表示灰階的深度，數字越小代表顏色越深。中間是一個 3x3 的 filter，在有些地方會被稱為 kernel，但這門課都會稱作 filter。這樣的兩個 matrix 做 convolution 運算後（用 * 表示），會產生一個 4x4 的 matrix。

運算方法則是，將 3x3 的 filter 與圖片的左上方 match（如圖片淺藍底），對應到的格子相乘，最後再將九個數字相加。依序移動 3x3 的 filter，如此最後就會產生一個 4x4 的 matrix。

![convolution operation result.png]({{ "/img/posts/convolution operation result.png" | absolute_url }}){:height="150px" width="210px"}

而中間的 filter 可以看到是一個由左至右從淺到深的圖。因為現在做的是 Vertical edge detection，所以才會選擇這樣的 filter。

再看一個例子，
![vertical edge detection.png]({{ "/img/posts/vertical edge detection.png" | absolute_url }}){:height="400px" width="600px"}

我們可以看到，最右邊最後產生的是一個中間一條白色的圖，這就偵測到了我們的想找垂直邊緣的圖（最左邊）的正中間有個邊界。（這個例子看起來邊緣很寬，是因為我們這個圖只有 6x6，如果今天用大一點的圖 1000x1000 就會發現這樣的偵測效果是很好的）

***

**Different transitions**
![vertical detection different transitions.png]({{ "/img/posts/vertical detection different transitions.png" | absolute_url }}){:height="400px" width="600px"}

剛剛的例子是由亮到暗（上），現在的例子是由暗到亮（下），會發現時候最後運算出來的 matrix 也會不同，根據中間的數字我們可以知道，這張圖是由亮到暗還是由暗到亮。下圖的中間偵測得到邊緣數字是 -30，如果今天需要偵測的結果需要知道深淺的變化，那數字就是重要的，但如果今天只是要抓邊緣，也可以將 -30 取絕對值，一樣能抓到轉換的邊界。

***

**Vertical and horizontal edge detection**
看完了垂直的範例，我們再看一下偵測水平邊緣的 filter。
![vertical and horizontal detection.png]({{ "/img/posts/vertical and horizontal detection.png" | absolute_url }}){:height="400px" width="600px"}

***

**Different filters**
從上面的結果可以發現，不同的 filter 可以讓我們偵測出不同的狀況。這邊提了一下兩個 filter，Sobel filter 和 Scharr filter。其實我們可以不需要直接使用現成的 filter，而是可以訓練出一個 filter 針對我們的需求，這之後會再提。

***

Reference:
<br>
[Coursera - Convolutional Neural Networks(deeplearning.ai)](https://www.coursera.org/learn/convolutional-neural-networks/home/welcome)