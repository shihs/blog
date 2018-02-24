---
layout: post
title: "[R]在 R 中使用 system 呼叫 python"
author: "Shihs"
---

我個人比較偏好使用R做所有的事情，
但某些時候還是需要使用到python，
所以希望可以在R上呼叫python程式碼。

一開始我找到了rPython這個library，
但它似乎無法在windows上使用......
所以我又找到了另一個不需要安裝任何套件且可以在windows上執行的辦法！


```R
system("python python_script.py")
```

這個辦法是呼叫系統函數，
就像是在cmd上面打的指令一樣，
而且在mac上也可以執行！

