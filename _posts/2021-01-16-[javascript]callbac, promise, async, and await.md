---
layout: post
comments: true
title: "[javascript]同步 v.s. 非同步與callback, promise, async, and await"
date: 2021-01-16 16:49
author: "Shihs"
category: [javascript]
---

之前因為在學 node.js 寫過[一篇文章](https://shihs.github.io/blog/javascript/node.js/2020/07/27/node.js-callback/)介紹同步非同步以及 callback，但之前沒有實際使用的經驗，有點懵懵懂懂，現在有了一些實際的應用的範例，所以想要再重新整理一次，並加上 promise、async, 與 await。

***

JavaScript Engine 是以單執行緒（單線程/Single Thread）且同步（Synchronous）的方式執行。

## 同步（Synchronous）

- 指程式必須等待前面的程式執行完才能執行。

## 非同步（Asynchronous）

- 指程式不須等待前面的程式執行完就能執行。

**note**
- 執行緒（thread）：執行緒是比程序（process）更小的單元，它是 CPU 的最小執行單元。是作業系統能夠進行運算排程的最小單位。一個程序（process），至少包含一個或多個執行緒。[(source)](https://medium.com/@yining1204/javascript-核心篇-學習筆記-chap-15-執行緒與同步-非同步-107802469752)

- 單執行緒：單執行的特性是**順序執行**，當遇到比較耗時的任務時，還未執行的任務就會處於等待狀態，一定要等到前面的任務完成了，才會往後執行。[(source)](https://medium.com/@yining1204/javascript-核心篇-學習筆記-chap-15-執行緒與同步-非同步-107802469752)

因為 JavaScript 是以單執行緒且同步的方式去執行，它在執行程式碼的時候會按照順序將程式碼片段在堆疊中（stack）執行，而且一次只會執行一個程式碼片段（one thing at a time），只是當碰到非同步（Asynchronous）的任務時，會把它往後放，放到事件佇列(Event Queue)中，等所有的任務完成後才會回來執行。以下面程式碼為例，

```javascript
// setTimeout(callbackFunction, timeToDelay)
setTimeout(() => {
  console.log('a');
}, 0);
console.log('b');
```

印出來的結果會是

```
b
a
```

`setTimeout` 是一個非同步的 Web API，JavaScript 執行到這段的時候會將 `setTimeout` 放到 Event Queue 中等待，等 stack 中的任務都執行完才回來執行，所以會先印出`b`再印`a`。

***

## Callback

callback 是 javascript 中很常見的一種使用方式，它讓函式可以當成參數傳進另一個參數中使用，讓我們可以控制程式碼的流程。看以下範例，

```javascript
function test() {
    console.log("This test function is done.");
}
function main(callback) {
    console.log("This is main start.");
    callback();
    console.log("This is main end.");
}
main(test);
// This is main start.
// This test function is done.
// This is main end.
```

但其實更多時候 callback 會牽扯到非同步 API 的狀況，像是下面的例子，

```javascript
function test() {
    // 這邊模擬 test 這個 function 去 call 其他 API 要等待的情況
    // 等了一秒後才會執行 console.log 這個函式
    setTimeout(()=> {
        console.log("This test function is done.");
    }, 1000);
}
function main(callback) {
    console.log("This is main start.");
    callback();
    console.log("This is main end.");
}
main(test);
// This is main start.
// This is main end.
// This test function is done.
```

這次`callback()`因為會有等待的情況，所以後面的 "This is main end." 先被執行完。那假如想要`callback()`執行完才執行下一行該怎麼做呢？（譬如說，這個`callback()`在做的是使用`XMLHttpRequest()`送 request 給某個網頁，而下面的程式碼必須等待網頁的 response 才可以執行下面的程式碼。）這時候只要把，執行 "This is main end." 這行程式碼也當成 callback() 傳進去就行了。

```javascript
function test(callback2) {
    // 這邊模擬 test 這個 function 去 call 其他 API 要等待的情況
    // 等了一秒後才會執行 console.log 這個函式
    setTimeout(() => {
        console.log("This test function is done.");
        callback2();
    }, 1000);
}
function main(callback) {
    console.log("This is main start.");
    callback(() => {
        console.log("This is main end.");
    });
}
main(test);
// This is main start.
// This test function is done.
// This is main end.
```

所以 callback 可以用來解決非同步的問題，但是當 callback 越來越多，就會形成 `callback hell`，就像是下面這樣，

```javascript
function api1(callback) {
    setTimeout(() => {
        console.log("Done with api1");
        callback();
    }, 2000);
}
function api2(callback) {
    setTimeout(() => {
        console.log("Done with api2");
        callback();
    }, 1000);
}
function main(callback) {
    api1(() => {
        api2(() => {
            callback();
        });
    });
}
main(() => {
    console.log("All function is done.");
});
// "Done with api1"
// "Done with api2"
// "All function is done."
```

甚至變成

```javascript
api1(() => {
    api2(() => {
        api3(() => {
            api4(() => {
                // bla bla bla
            });
        });
    });
});
```

***

## Promise

Promise 也是一個可以用來處理非同步操作的東西。Promise 通常包括三種狀態：`resolve`、`reject`和`pending`。`resolve`代表成功，`rejetc`代表失敗，`pending`代表還在處理中, 結束狀態未知。`then()`方法可以回傳`Promise`物件。

例如，現在想要使用`XMLHttpRequest()` API傳送 request，我們需要等待 response 後才有後續動作。

```javascript
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function sendHttp() {
	url = "https://www.google.com/";
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url);
	xhr.responseType = "document";
	xhr.send();

	// 如果沒等待 response，status 和 response 會是 0 和 null
	// console.log(xhr.status);
	// console.log(xhr.response);

	sleep(2000).then((result) => {
		console.log(xhr.status);
		console.log(xhr.response);
	});
}

sendHttp();
```

`then()` 其實是可以一直往後加，就是像`callback`，想要前面的事情做完，才做下面，形成 Promise Chain，但這樣就又會變成 then hell。所以這時候出現了 async 和 await，讓程式碼看起來更容易閱讀。


***

## Async/Await

async/await 還是會用到 promise，但不使用 then 去啟動。像剛剛上面的例子，可以改寫成下面這樣，


```javascript
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function sendHttp() {
	url = "https://www.google.com/";
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url);
	xhr.responseType = "document";
	xhr.send();

	await sleep(2000);
	// 如果需要更多 sleep(2000)
	// await sleep(2000);
		
	console.log(xhr.status);
	console.log(xhr.response);
}

sendHttp();
```

在`sendHttp()`這個 function 前加上 async，並在`sleep(2000)`前加上 await 就好，整體畫面看起來是不是容易閱讀很多？如果需要更多的`sleep(2000)`，只需要多加 await 往下寫就好，整個畫面看起來容易閱讀很多。


***

**Reference:**
<br>
[非同步(Asynchronous)與同步(Synchronous)的差異](https://medium.com/@hyWang/%E9%9D%9E%E5%90%8C%E6%AD%A5-asynchronous-%E8%88%87%E5%90%8C%E6%AD%A5-synchronous-%E7%9A%84%E5%B7%AE%E7%95%B0-c7f99b9a298a)
<br>
[世界上誤解最大的語言 JavaScript 之 JS 到底是同步與非同步語言?!](https://hsiangfeng.github.io/javascript/20191209/1271823341/)
<br>
[[筆記] 理解 JavaScript 中的事件循環、堆疊、佇列和併發模式（Learn event loop, stack, queue, and concurrency mode of JavaScript in depth）](https://pjchender.blogspot.com/2017/08/javascript-learn-event-loop-stack-queue.html)
<br>
[callback, promise, async/await 使用方式教學以及介紹 Part I](https://yu-jack.github.io/2018/07/22/promise/)








