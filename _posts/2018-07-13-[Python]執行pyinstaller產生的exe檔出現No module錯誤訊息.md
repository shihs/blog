---
layout: post
comments: true
title: "[Python]執行pyinstaller產生的執行檔出現No module錯誤訊息"
date: 2018-07-13 11:56
author: "Shihs"
category: [Python]
---

前面介紹過使用 [pyinstaller 將 .py 打包成執行檔](https://shihs.github.io/blog/python/2018/05/24/Python-使用pyinstaller套件打包.py檔/)，方便使用者執行程式。

我在 mac 終端機輸入 `pyinstaller -F pyscript.py` 後， <br>
執行在 dist 資料夾底下的檔案，卻出現
`
no module named 'somepackagename'
`
的錯誤訊息。


這表示，在打包這支程式時，並未把需要的套件打包進去？ <br>
但是我使用 .py 執行時並沒有這樣的問題啊？ <br>
表示我的電腦確實是有安裝該套件才是。

原來是因為在打包時 pyinstaller 並不知道這個套件的路徑， <br>
所以只要加上套件的路徑位置，讓 pyinstaller 執行打包時可以找得到就好。 <br>

假如缺少的套件在 `/usr/local/lib/python2.7/site-packages`， <br>

只要將原本的 <br>
`pyinstaller -F pyscript.py` <br>

改成 <br>
`pyinstaller -F -p /usr/local/lib/python2.7/site-packages pyscript.py` <br>

就好了。 <br>


可以用， <br>
```python
import sys
print sys.path
```
查看系統路徑，就可以知道套件可能的位置。



