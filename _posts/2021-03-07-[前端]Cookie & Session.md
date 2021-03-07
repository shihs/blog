---
layout: post
comments: true
title: "[前端]Cookie & Session"
date: 2021-03-07 15:08
author: "Shihs"
category: [前端]
---

在邊閱讀網路資訊的時候，我對於 cookie 和 session 從覺得理解到感到困惑，到後來又覺得好像懂了，但也許不是百分之百正確。我盡量把理解的東西寫下來，但如果有任何錯誤，歡迎指正。

***

### 重點

Session 和 Cookie 的目的是用來讓 Sever 知道 Client 的狀態，而 Cookie 是將狀態資料存在 Client 端（Browser），而 Session 則是將資料存在 Server 端（e.g Redis）

***

### HTTP 的 stateless（無狀態）

前面說到「Session 和 Cookie 的目的是用來讓 Sever 知道 Client 的狀態」，但

1. 為什麼 Server 不知道 Client 的狀態呢？
2. 為什麼需要讓 Sever 知道 Client 的狀態呢？

![HTTP Model](http://wiki.hashphp.org/images/6/67/HTTP_Model.jpg){:width="50%" heigh="50%"}


要回答第一個問題，就要先知道「**HTTP 是 stateless（無狀態）**」，而 stateless（無狀態）的定義是

- Server 和 Client 不會記住（retain）之前的連線 
- 每個 Client 送出的 request 都被視為是唯一且獨立的 connection

舉個例子，

[https://dotblogs.com.tw/jimmyyu/2010/10/16/difference-between-stateful-and-stateless](https://dotblogs.com.tw/jimmyyu/2010/10/16/difference-between-stateful-and-stateless)

上面這個網址是我在搜尋「無狀態」時找到覺得解釋得不錯的部落格，而我從我的瀏覽器打開這個網頁，和你從你的瀏覽器輸入這個網址打開，基本是上一樣的，並不需要先連到其他網頁，像這樣子的情況就稱為 stateless（無狀態）。

解決第一個問題後，那 stateless 就 stateless 啊，為什麼要讓 Server 知道 Client 的狀態呢？

想想看，我們在使用 facebook 或是 instagram 等等很多網站都必須要先登入後才能觀看到想看到的頁面；或是，在網拍網站上如果我們把東西加到購物車，當下次登入時打開，還能夠看到上次加入的商品。但以剛剛 stateless（無狀態）的邏輯來思考，這件事情是不可能可以達成的，因為假如每次的 request 都是獨立且唯一的，那這樣每一次重新點選網頁都會是一個新的事件，Server 就像是失憶一樣，根本不會記得曾經發生過什麼事情，所以當 Client 端做了改變（ex. 登入、商品加入購物車...等等），Sever 端並不會知道，當我們想要做任何事情，每一次都必須要重新來一遍才行。

這就是為什麼我們會想要讓 Server 知道 Client 的狀態了（Stateful）。

***

### Cookie 是什麼？

Cookie 是用來記錄 Client 與 Server 目前的溝通狀態，會以 name-value 的形式呈現，並且存在 Client 端。

![進入 googlec.com 後得到的 cookie]({{ "/img/posts/cookie.png" |absolute_url}}){:width="80%" heigh="80%"}


而這個 cookie 在 Client 端第一次發送 request 後，Server 會以 `Set-Cookie` 的方式寫在 response header，回應給 Client，而 Client 瀏覽器就會將這個 Cookie 存在本機端，下一次要再次送 request 時，會把這個已儲存的 Cookie 已 `Cookie` 的方式存在 resquest header 和 request 一起送出，讓 Sever 知道這個 Client 目前的狀態。（可以用 Chrome 的開法者模式看 network 中網頁的 Response Headers 和 Request Headers 找到 `Set-Cookie` 和 `Cookie`）

但這樣儲存 Cookie 又會有什麼問題呢？

1. Cookie size 的限制：根據 RFC-2965 的規定，一個 Cookie 最大只能是 4096 bytes。

2. 佔據網路流量：由於每次 request 都會傳送 Cookie 資料，所以當 Cookie 資料越來越大，request 傳輸的資訊也會更著變大，這樣就會影響網路傳輸的速度。

3. Cookie 可能被 Client 竄改：由於 Cookie 存在 Client 端，所以 Client 是可以完整的看到 Cookie 資料的，那如果 Cookie 竄改或者是外洩，這樣就存在著資安的風險。

根據以上的問題，我們可以知道，Cookie 中不能存放有資安疑慮的資料，也不能存放太大的資訊量。所以為了彌補這些不足，就有了 Session 的出現。


***

### Session 是什麼？

Session 是一種比 Cookie 更安全的狀態管理機制。

既然 Session 是為了彌補 Cookie 的不足，它就必須要解決上面提到的 Cookie 可能會有的問題。所以 Session 會將狀態資訊存在 Sever 端，以避免 Client 端可以任意修改資訊，此方法也能避免儲存與傳輸的資料過大的問題。

而為了要讓 Client 端知道 Session 儲存的資訊，Server 端會在 response 的 Cookie 中回傳一組 SessionID 讓 Client 儲存在 Cookie 裡，當下次 Client 送出 request 時，就在 Cookie 裡一起送出這組 SessionID，而 Server 就可以透過這組 SessionID 去驗證這個 Client 身份，並知道上一次儲存的狀態，然後回傳內容。



***

**Reference:**
<br>
[前端三十｜27. [WEB] Cookie & Session 是什麼？](https://hulitw.medium.com/session-and-cookie-15e47ed838bc)
<br>
[[ASP.NET]Stateful與Stateless](https://dotblogs.com.tw/jimmyyu/2010/10/16/difference-between-stateful-and-stateless)
<br>
[白話 Session 與 Cookie：從經營雜貨店開始](https://hulitw.medium.com/session-and-cookie-15e47ed838bc)
<br>
[淺談 Authentication 上集：Cookie 與 Session 介紹](https://medium.com/@vicxu/authentication-那些小事上集-cookie-與-session-介紹-1da2d413afa2)



