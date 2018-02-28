---
layout: post
title: "[R]Error when saving xlsx workbook with package openxlsx"
date: 2017-06-22 11:55
author: "Shihs"
---

如果在windows系統使用saveWorkbook()出現以下錯誤訊息
```
Error: zipping up workbook failed. Please make sure Rtools is installed or a zip application is     available to R.
Try installr::install.rtools() on Windows.
installr::install.rtools()
No need to install Rtools - You've got the relevant version of Rtools installed
saveWorkbook(wb, file = "dq", overwrite = TRUE)
Error: zipping up workbook failed. Please make sure Rtools is installed or a zip application is available to R.
Try installr::install.rtools() on Windows.
```

1.[安裝Rtools.exe](https://cran.r-project.org/bin/windows/Rtools/)

2.找到Rtools底下的zip.exe路徑，
並設定rools的zip.exe路徑即可解決此問題
```R
Sys.setenv("R_ZIPCMD" = "C:/Rtools/bin/zip.exe") ## path to zip.exe
```




