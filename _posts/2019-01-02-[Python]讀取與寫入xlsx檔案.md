---
layout: post
comments: true
title: "[Python]讀取與寫入xlsx檔案"
date: 2019-01-02 11:49
author: "Shihs"
category: [Python]
---

這裡要介紹使用 pandas 套件讀取與寫入 xlsx 檔案。

在開始前請先安裝 pandas 套件，
```
pip install pandas
```

***

**讀取檔案**

```python
df = pd.read_excel("filename.xlsx", header = None)

# 獲取列數
rows = df.shape[0]

# 獲取儲存格內容
df.iat[1, 0]

# 修改儲存格內容
df.iloc[1, 0] = "test"
# 但修改後必須要儲存才會修正檔案內容
# df.to_excel('test_result.xlsx', sheet_name = 'sheet1')
```

若在執行以上程式碼時產生錯誤訊息：
```
Pandas pd.read_excel giving ImportError: Install xlrd >= 0.9.0 for Excel support
```

這時候只要安裝 xlrd 套件就能解決問題。
```
pip install xlrd
```

***

**寫入檔案**

```python
import pandas as pd

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
```

以上的程式碼是參考[這裡](https://xlsxwriter.readthedocs.io/example_pandas_simple.html#)。

我存的檔案內容是中文，這時候產生了像這樣的錯誤訊息
```
Python pandas to excel UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 11
```
只要將 `pd.ExcelWriter` 裡的參數 `engine='xlsxwriter'` 改成 `engine='openpyxl'` 就可以了。



***

Reference:
<br>
[Example: Pandas Excel example](https://xlsxwriter.readthedocs.io/example_pandas_simple.html)
<br>
[Python: Pandas pd.read_excel giving ImportError: Install xlrd >= 0.9.0 for Excel support](https://stackoverflow.com/questions/48066517/python-pandas-pd-read-excel-giving-importerror-install-xlrd-0-9-0-for-excel)
<br>
[Python pandas to excel UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 11](https://stackoverflow.com/questions/47698744/python-pandas-to-excel-unicodedecodeerror-ascii-codec-cant-decode-byte-0xe2)
<br>
[PYTHON pandas 操作Excel 基本介紹](https://ithelp.ithome.com.tw/articles/10197119)

