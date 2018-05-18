---
layout: post
comments: true
title: "[R]使用 R 寄Outlook Email"
date: 2018-02-26 18:45
author: "Shihs"
category: R
---

之前有介紹過使用mailR這個套件夾帶檔案[使用gmail信箱發送信件](https://shihs.github.io/blog/2016/07/17/R-%E4%BD%BF%E7%94%A8R%E7%99%BC%E9%80%81email/)。<br>


這篇要介紹使用RDOCOMClient這個套件來發送outlook夾帶檔案的電子郵件。<br>
[參考](https://stackoverflow.com/questions/26811679/sending-email-in-r-via-outlook)


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