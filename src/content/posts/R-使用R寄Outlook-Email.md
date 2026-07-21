---
title: '[R]使用 R 寄Outlook Email'
date: '2018-02-26'
categories:
  - R
slug: R-使用R寄Outlook-Email
---

之前有介紹過使用mailR這個套件夾帶檔案<a href="https://shihs.github.io/blog/r/2016/07/17/R-使用R發送email/" target="_blank">使用gmail信箱發送信件</a>。<br>


這篇要介紹使用RDOCOMClient這個套件來發送outlook夾帶檔案的電子郵件。<br>
<a href="https://stackoverflow.com/questions/26811679/sending-email-in-r-via-outlook" target="_blank">參考</a>


```R
library(RDCOMClient)
## init com api
OutApp <- COMCreate("Outlook.Application")
## create an email 
outMail = OutApp$CreateItem(0)
## configure  email parameter 
outMail[["To"]] = "reciever@mail.com"
outMail[["subject"]] = "subject"
# There are two ways you can write for mail body
# First:text
# outMail[["body"]] = 
# "Dear reciever,
#                      
# Please see attached.
# 
# 
# Best regards,
# Sender"

# Second:html text
body <- 
'
<p>Dear reciever,</p>
<p>Please see attached.</p>
<br>
<br>
<p>Best regards,
<p>Sender</p>'

outMail[["HTMLbody"]] = body

# attachment
outMail[["Attachments"]]$Add("path of your attachment")
## send it                     
outMail$Send()


```
