---
layout: post
title: "[Excel][VBA]寄出內文含圖檔的outlook信件"
date: 2017-07-05 16:12
author: "Shihs"
category: [Excel, VBA]
---

這裡要介紹如何使用Excel VBA<br>
在信件內容包含截取sheet中的特定欄位區塊，<br>
並將此區塊變為圖檔包含在內文中寄出。<br>

現在要截取一份長這樣的檔案<br>
![擷取.PNG](http://user-image.logdown.io/user/13067/blog/12306/post/2007909/E6x1745kT82DMCqRbLq2_%E6%93%B7%E5%8F%96.PNG)
有兩種方法。<br>



第一種方法是，<br>
先將截取的區塊存成圖檔後再將此圖檔讀取到郵件內容。<br>


```VBA
Sub PrintScreen()

      '複製工作表要存圖檔的範圍
        Sheets("Sheet1").Select
        Set rng = Range("A1:B3")
        rng.CopyPicture

      ' Excel 存圖檔的精簡程式碼。
        With ActiveSheet.ChartObjects.Add(1, 1, rng.Width, rng.Height)  '新增 圖表
            .Chart.Paste                                                '貼上 圖片
            .Chart.Export Filename:="test.PNG", Filtername:="PNG" '匯出 圖片
            .Delete                                                     '刪除 圖表
        End With

End Sub

Sub SendMail_1()
    
    Dim objOutlook As Object
    Dim objMail As Object
    
    Set objOutlook = CreateObject("Outlook.Application")
    Set objMail = objOutlook.CreateItem(0)
    
    With objMail
        .to = "address@email.com"
        .Subject = "Subject"
        .Body = "mail body"
        .HTMLbody = .HTMLbody & "<br><B>Embedded Image:</B><br>" _
                & "<img src='test.PNG'" & "width='250' height='100'><br>" _
                & "<br>Best Regards, <br>Sumit</font></span>"
       ' objMail.Attachments.Add "test.PNG"       ' 使用附件檔案
       '.Display     ' 可以編輯郵件內容，再按下 傳送 鍵。
       '.Save         ' to save a copy in the drafts folder
        .Send        ' 直接送出郵件
        
    End With       
    
    Set objOutlook = Nothing
    Set objMail = Nothing
    
End Sub

```

第二種方法是，<br>
直接截取區要的區塊，變成圖檔，然後貼到信件內容。

```VBA
Sub SendMail_2()

    Set objOutlook = CreateObject("Outlook.Application")
    Set objMail = objOutlook.CreateItem(0)

    ' mail body
    strbody = "mail body<br><br><br><br><br><br>"

    'Copy range of interest
    Dim r As Range
    Set r = Sheets("Sheet1").Range("A1:B3")
    r.Copy

    'Paste as picture in sheet and cut immediately
    Dim p As Picture
    Set p = ActiveSheet.Pictures.Paste
    p.Cut
        
    With objMail
        .to = "address@email.com"
        '.cc =
        '.bcc = ""
        .Subject = "Subject"
        .HTMLbody = strbody
        '.Display
        
    End With


    'Get its Word editor
    objMail.Display
    Dim wordDoc As Object
    Set wordDoc = objMail.GetInspector.WordEditor

    'Paste picture
    wordDoc.Range(Start:=wordDoc.Range.End - 3).Paste
    
    'send mail
    objMail.Send
    
    Set objOutlook = Nothing
    Set objMail = Nothing

End Sub

```

