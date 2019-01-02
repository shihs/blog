---
layout: post
comments: true
title: "[Python]pyinstaller出現錯誤訊息AttributeError:type object pandas._TSObject has no attribute _reduce_cython_"
date: 2019-01-02 12:47
author: "Shihs"
category: [Python]
---

在打包含有 pandas 套件的程式碼時產生了以下的錯誤訊息，
![pyinstaller pandas.png]({{ "/img/posts/pyinstaller pandas.png" | absolute_url }}){:height="400px" width="580px"}

根據[Hooks: Add hook-pandas.py to fix issue #2978. #2998](https://github.com/pyinstaller/pyinstaller/pull/2998)的討論串，有人回答
```
when run pyinstaller -F xxx.py in windows10 , I get error AttributeError: type object 'pandas._libs.tslib._TSObject' has no attribute '__reduce_cython__', and solve it by degrade pandas version to 0.20.0.
```

我將 pandas 套件的版本降至 0.20.3 也確實解決問題了。

先檢查一下 pandas 版本
```
pip show pandas
```

將版本降至 0.20.3
```
pip install pandas==0.20.3
```

這時候打包完後執行應該就不會有問題了！

***

Reference:
<br>
[Hooks: Add hook-pandas.py to fix issue #2978. #2998](https://github.com/pyinstaller/pyinstaller/pull/2998)
<br>
[成功解决pyinstaller打包AttributeError:type object pandas._TSObject has no attribute _reduce_cython_](https://blog.csdn.net/qq_41185868/article/details/80601983)