---
layout: post
title: "[Python]Google 翻譯 API 接口 googletrnas"
date: 2018-01-15 22:00
author: "Shihs"
category: Python
---

使用前，先安裝[googletrans](https://py-googletrans.readthedocs.io/en/latest/)
```cmd
# windows
pip install googletrans
```
```
# mac
sudo pip install googletrans
```


程式碼
```python
# -*- coding: utf-8 -*-

from googletrans import Translator
import sys

# 這兩行很重要，不然會有編碼問題
reload(sys)
sys.setdefaultencoding( "utf-8" )

translator = Translator()
# src來源語言，dest要翻譯語言，如果要找其他語言可以參考說明文件
print translator.translate('고마워', src = "ko", dest = "zh-TW")

```

根據說明文件，這個套件可能會有不穩定的問題
找到有人[直接爬google翻譯的程式碼](https://hk.saowen.com/a/4c76af2381e3a60e86f7c4b934a21faebad8b2e7b4a4131cb7c2889afcea6479)
但其實如果沒有要很大量的爬取我認為這個套件應該很好用了。





