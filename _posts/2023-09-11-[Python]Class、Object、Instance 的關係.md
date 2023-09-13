---
layout: post
comments: true
title: "[Python]Class、Object、Instance 的關係"
date: 2023-09-11 21:06
author: "Shihs"
category: [Python]
---

Python 是一個物件導向（Object Oriented Programming, OOP）的程式語言，在物件導向中最重要的就是 Class、Object、Instance 的關係，以下將用 Python 說明舉例這三者的關係。

![](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_9e90f720f902522104f2bb6de3440fee.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1694624187&Signature=PXuzpk3ngOOF%2FukTmVNOf3sujiQ%3D)
圖片來源：[[Python 基礎教學] 一切皆為物件，到底什麼是物件 Object ?](https://www.maxlist.xyz/2021/01/11/python-object/)

先用兩段話來說明三者的關係：
>A **Class** is the template/blueprint for building actual **instances** of **Object**.

>An **Object** is an **instance** of a **Class**. A class is like a blueprint while an instance is a copy of the class with actual values.

針對 Class、Object、Instance 的個別解釋：

**Class**
- Classes are blueprint for creating objects.
- Classes define properties (attributes) and behaviours (methods) that every **instance** of the class should have.

**Object**
- An **Object** is an **instance** of a **Class**, carrying its own set of attributes and methods defined by the Class.

**Instance** 
- A instance is an individual object of a certain Class.

舉一個例子來解釋 Class、Object、Instance 的關係：我們把有四條腿、有尾巴、會汪汪叫的動物都歸類（class）為「狗」，所以當我們看到有四條腿、有尾巴、會汪汪叫的動物就會知道這些 objects 屬於「狗」這個類別（class）。今天我養了一隻叫做「同學」的狗，「同學」這個 obejct 就會是「狗」這個類別（class）的一個實際的例子（instance）。

我的理解是，instance 是ㄧ個「特定」的 object（我的狗「同學」這個 instance 是特定的 object），而某個 class 的 objects 則是表示所有由該 class 建立出來的 instances；因此，有些時候 object 和 instance 是可以替換的。

不管今天是你的狗小白、他的狗小黑、還是我的狗同學，都是「狗」這個 class 的 object。而所有的狗都是「狗」的類別（class）的實際的例子（instance），他們就一定會有所有「狗」該有的特性（我們這邊舉例正常情況下的狗），像是有腿、有尾巴、會汪汪叫，所以他們都是「狗」這個類別的 object。而當特別指名你的狗「小黑」就是在說「小黑」這個 instance。

---

### 範例：狗
將上述的「狗」寫成 python code 來說明 Class、Object、Instance 的觀念

**建立一個「狗」Class**
```python=
class Dog:
    def __init__(self):
        self.legs = 4
        self.has_tail = True
```

上面的程式碼是 `Dog` 的 **class**，`__init__` 則是一個新的 instance 被建立（或是說 object 被建立）時這個 `__init__` method 會自動執行。（It's often referred to as a **constructor** because it's used to set up or initialize attributes for a new object.）。


通常用來給定這個新的 instance 的狀態，上面程式碼的範例則是給予 `legs` 和 `has_tail` 兩個 attribute，並且定義為 4 和 True。

**建立一個 Object**

在 Python 中，可以使用以下的方式建立一個 Object，或是說 Instance。

```python
同學 = Dog()
```

上面的 `同學` 就是一個 `Dog` Class 的 Object，或是說一個 Instance。

**Class 的 method**

```python
class Dog:
    def __init__(self):
        self.legs = 4
        self.has_tail = True
    def bark(self):
        print("汪汪！")
```

`bark` method 會發出「汪汪」的叫聲。

以下是程式碼實際的結果：
![](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_d7b06b9b166ffecfc050f81f82044241.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1694624324&Signature=ZBrQflNYFWYs5TxUaQeLMwXlFQQ%3D){:width="30%" heigh="30%"}

上面的 `mydog` 是 Dog class 的 instance，也是一個 class 的 object，當 `mydog` 這個 instance 建立的時候就會有 **legs** 和 **has_tail** 這兩個屬性（attributions），並且還有一個定義的 **bark** method。

---

**Reference**
- [那個OOP裡頭class、object、instance間複雜的三角關係](https://vocus.cc/article/640bde92fd8978000138c9fa)
- [Python Object Oriented Programming (OOP) - with examples](https://www.packetswitch.co.uk/python-object-oriented-programming/)
- [[Python 基礎教學] 一切皆為物件，到底什麼是物件 Object ?](https://www.maxlist.xyz/2021/01/11/python-object/)
