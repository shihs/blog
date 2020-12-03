---
layout: post
comments: true
title: "[javascript]Traversing the DOM"
date: 2020-12-03 13:39
author: "Shihs"
category: [javascript]
---

整理 Treehouse 前端課程中 [JavaScript and the DOM](https://teamtreehouse.com/library/javascript-and-the-dom-2) 的最後一節 Traversing the DOM 內容。

DOM Traversal 的意思是，可以透過一個 element 與這個 element 的關係去選取其他的 element。

***

## parentNode

- **parentNode**：顧名思義，選取被選取的 element 的 parent node。

```javascript
// 選取 id 為 myParagraph 的 node
let paragraph = document.getElementbyId('myParagraph'); 

// 使用 paragraph 選取它的 parent node
let parent = paragraph.parenNode; 

// 可以直接利用這個 parent node 做些事
parent.removeChild(paragraph); // 刪除 paragraph node
```

***

## previousElementSibling & insertBefore

- **previousElementSibling**：選取被選取的 element 前一個的 sibling。
- **insertBefore**：將被選取的 element 插入在某一個 element 之前， `let insertedNode = parentNode.insertBefore(newNode, referenceNode)`

**previousSibling v.s. previousSibling**

為什麼 sibling 要特別加上 'Element' 呢？因為如果使用 `previousSibling` 他會抓取前一個 sibling node，不管它是什麼。而我們[前一篇](https://shihs.github.io/blog/html/2020/11/13/HTML-%E6%96%87%E4%BB%B6%E7%89%A9%E4%BB%B6%E6%A8%A1%E5%9E%8B-Document-Object-Model/)講過， node 包含 document、element、attribute 和 text。所以使用 `previousElementSibling` 我們就只會抓前面的 element sibling。


在課程的範例中，現在想要按了 Up 按鈕之後，該 <li> 就會上移。
```html
<ul>
  <li>grapes 
    <button class="up">Up</button>
    <button class="remove">Remove</button>
  </li>
  <li>amethyst 
    <button class="up">Up</button>
    <button class="remove">Remove</button>
  </li>
  <li>lavender 
    <button class="up">Up</button>
    <button class="remove">Remove</button>
  </li>
  <li>plums 
    <button class="up">Up</button>
    <button class="remove">Remove</button>
  </li>
</ul>
```


```javascript
// 選取 ul 的 tag
const listDiv = document.querySelector('.list');
const listUl = listDiv.querySelector('ul');

// 按下 up 按鈕之後，該 li tag 會往上移
listUl.addEventListener('click', (event) => {
  if(event.target.className == 'up') {
  	// 被 click 的 button 的 parent node 就是 li
    let li = event.target.parentNode; 
    // 被選取的 li tag 的 previous element sibiling，也就是前一個 li tag
    let prevLi = li.previousElementSibling; 
    // 這個 li 的 parent node
    let ul = li.parentNode; 
    // 如果 prevLi 不是 null，換句話說，不是第一個
    if (prevLi) {
      // 將被選取的 li tag 往前移
      ul.insertBefore(li, prevLi); 
    }
  }
});

```

***

## nextElementSibling & insertBefore

按了 down button 之後，該 li 往下移。基本上概念和剛剛上面往前一是一樣的，只是現在使用 nextElementSibling，去選取後面的 element。


```html
<ul>
  <li>grapes 
    <button class="up">Up</button>
    <button class="down">Down</button>
    <button class="remove">Remove</button>
  </li>
  <li>amethyst 
    <button class="up">Up</button>
    <button class="down">Down</button>
    <button class="remove">Remove</button>
  </li>
  <li>lavender 
    <button class="up">Up</button>
    <button class="down">Down</button>
    <button class="remove">Remove</button>
  </li>
  <li>plums 
    <button class="up">Up</button>
    <button class="down">Down</button>
    <button class="remove">Remove</button>
  </li>
</ul>
```


```javascript
// 選取 ul 的 tag
const listDiv = document.querySelector('.list');
const listUl = listDiv.querySelector('ul');

// 按下 up 按鈕之後，該 li tag 會往上移
listUl.addEventListener('click', (event) => {
  if(event.target.className == 'down') {
    let li = event.target.parentNode;
    let nextLi = li.nextElementSibling;
    let ul = li.parentNode;
    if (nextLi) {
      ul.insertBefore(nextLi, li);
    }    
  }
});
```

***

## children

`.children` 可以選取該 element 底下所有的 child element。

```javascript
const listDiv = document.querySelector('.list');
const listUl = listDiv.querySelector('ul');

// lisUl 底下的 child，也就是 li tag
const lis = listUl.children;
```
***

## firstChild & lastChild v.s. firstElementChild & lastElementChild

選取該 element 的第一個或最後一個 child。同樣的，firstElementChild & lastElementChild 選取的會是 element。









