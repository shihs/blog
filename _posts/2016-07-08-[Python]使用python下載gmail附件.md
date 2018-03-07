---
layout: post
title: "[Python]使用 python 下載 gmail 附件"
date: 2016-07-08 21:02
author: "Shihs"
category: Python
---

每天都會收到信並且要利用信中的附件整理資料，
但這樣我在跑程式前還要手動去下載檔案，
覺得實在太麻煩，
所以找到了這個辦法！

因為我的mail是gamil，
所以以下的程式碼是針對gmail，
在執行前要先[打開imap](http://mobileai.net/2011/03/19/教您如何開啟-gmail-的-imap-功能/)
我主要是參考[這裡](https://gist.github.com/jasonrdsouza/1674794)


```python
import imaplib, inspect
import email
import os
from datetime import datetime
from email.header import decode_header

inspect.getmro(imaplib.IMAP4_SSL)
#與IMAP4 server連線，gmail要開啟IMAP
imap = imaplib.IMAP4_SSL('imap.gmail.com') 
#登入
imap.login('mymailaddress@gmail.com', 'mypasswd')
#選擇信箱標籤
imap.select("label")
#找所有mail
resp, mails = imap.search(None, "ALL")

#讀取信件內容，只抓取最新一封信件(len(mails[0].split())-1)
resp, data = imap.fetch(mails[0].split()[len(mails[0].split())-1], '(RFC822)')

emailbody = data[0][1]
mail = email.message_from_string(emailbody)

#找出含有附件的部分
for part in mail.walk():
	if part.get_content_maintype() == 'multipart':
		continue
	if part.get('Content-Disposition') is None:
		continue

	#附件檔名
	fileName = part.get_filename()  
	#修改檔名編碼<http://stackoverflow.com/questions/11206489/how-to-print-next-year-from-current-year-in-python>
	fileName = str(datetime.now().year - 1911) + str(decode_header(fileName)[0][0]).decode(decode_header(fileName)[0][1])
	if bool(fileName):
		filePath = os.path.join("C:\\Users\\mypc\\Desktop\\data", fileName)

		if not os.path.isfile(filePath) :
			fp = open(filePath, 'wb')
			fp.write(part.get_payload(decode=True))
			fp.close()
			print "attachement is downloaded!"
		else:
			print "file is already exist!"
			
#關閉連線與登出
imap.close()
imap.logout()


```