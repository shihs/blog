---
layout: post
comments: true
title: "[Database]ER Model 實體關聯模型"
date: 2020-01-01 20:56
author: "Shihs"
category: [Database]
---


## 實體關聯模型（Entity-Relationship Model）

是Conceptual model（概念塑模）的一環，用來描述**實體**與**實體**之間**關係**的工具。

|![ER Model.png]({{ "/img/posts/ER Model.png" |absolute_url}})|
|:--:| 
| [ER Model](http://www.csie.sju.edu.tw/cm/course/db/ch03.pdf) |

- 實體（Entity）：是指用以描述真實世界的物件，在關聯式資料庫中為一個「資料表」
  - 實體至少擁有一個不是鍵（主鍵）的屬性
  - 一個實體可以含有多個「屬性」(Attribute)用以描述該實體，在關聯式資料庫中，以資料表的「欄位」來表示
  - 例如：學生、員工、產品等等都是屬於實體
- 關係（Relationship）：指用來表示「一個實體」與「另一個實體」關聯的方式
  - 例如：一對一關係、一對多關係、多對多關係


***

## 實體（Entity）

**定義**
  - a ”thing” in the real world with an independent existence
  - 用來描述實際存在的事物（如:學生），也可以是邏輯抽象的概念（如:課程）
  - 必須可以被識別，亦即能夠清楚分辨出兩個不同的實體(an independent existence)
  - 以「名詞」的來命名，不可以是「形容詞」或「動詞」

**分類**
  - 實體(entity) 
  - 弱實體(weak entity)：必須依靠其他實體才能存在，若其依靠的實體消失，則該實體的存在也沒有意義了
    - 例如：學生家長就是依附在學生實體的弱實體，若學生不存在，則家長也沒有存在的意義

**圖示**

|![entity diagram.png]({{ "/img/posts/entity diagram.png" |absolute_url}})|
|:--:| 
| [Entity diagram](https://images.app.goo.gl/auQ9MAQCKttsdFGEA) |

***

## 屬性(Attribute)

**定義**
  - 用來描述實體的性質（Property）（就是關聯式表格的行）
    - 例如：學生的學號、名字、班級等等

**分類**
  - 多值屬性 vs 單值屬性
    - 多值屬性（Multivalued attributes）：屬性值不只一個時，我們稱該屬性為*多值屬性*
      - 例如：學生有多個專長，珠算、程式...
      - 關係圖中以「雙橢圓形」來表示
    - 單值屬性（Single-valued attribute）：非多值屬性稱為*單值屬性*
  
|![Multivalued attributes.png]({{ "/img/posts/Multivalued attributes.png" |absolute_url}})|
|:--:| 
| [多值屬性 Multivalued attributes diagram](http://spaces.isu.edu.tw/upload/19225/0/news/postfile_308.pdf) |


  - 複合屬性 vs 簡單屬性
    - 複合屬性（Composite attributes）：屬性由數個屬性所組成時，我們稱該屬性為*複合屬性*
      - 例如：姓名由姓、名組成
      - 關係圖如下
    - 簡單屬性（Simple attribute）：非複合屬性則稱為*簡單屬性*


|![Composite attributes.png]({{ "/img/posts/Composite attributes.png" |absolute_url}})|
|:--:| 
| [複合屬性 Composite attributes diagram](http://spaces.isu.edu.tw/upload/19225/0/news/postfile_308.pdf) |


  - 衍生屬性（Derived Attribute）
    - 它的值可以由其它屬性之值經由某種方式的計算或推論而獲得
    - 例如：年齡和星座可由生日推算出來


## 鍵屬性(Key attribute)

**定義**
 - 是指該屬性的值在某個環境下具有唯一性（primary key）


**圖示**

|![attribute.png]({{ "/img/posts/attribute.png" |absolute_url}})|
|:--:| 
| [Attribute diagram](https://images.app.goo.gl/auQ9MAQCKttsdFGEA) |

***


## 關係(Relationship)

**定義**
  - 是指用來表達兩個實體之間所隱含的關聯性
  - 使用足以說明關聯性質的「動詞」或「動詞片語」命名
    - 例如：『學生』與『系所』兩個實體型態間存在著一種關係─「就讀於」


**分類**
  - 關聯強度 Strength
    - 強關聯（strong relationship）：a relationship where entity is existence-independent of other entities, and PK of Child doesn’t contain PK component of Parent Entity
    - 弱關聯（weak (identifying) relationship）：a relationship where Child entity is existence-dependent on parent, and PK of Child Entity contains PK component of Parent Entity，也就是說，此關聯是連結*實體*與*弱實體*
  - Cardinality 
    - 1:1 一對一
    - 1:N 一對多
    - M:1 多對一
    - M:N 多對多
  - Participation constraints
    - 全部參與（Total participation）：every entity in the set is involved in the relationship
    - 部分參與（Partial participation）：not all entities in the set are involved in the relationship


**圖示**

|![Relationship.png]({{ "/img/posts/Relationship.png" |absolute_url}})|
|:--:| 
| [Relationship diagram](https://images.app.goo.gl/auQ9MAQCKttsdFGEA) |


***

**弱實體例子**

為了區分和一般實體的關係, 我們會以雙菱形來表示實體與弱實體之間的關係, 而弱實體和關係之間以雙直線連接


|![books.png]({{ "/img/posts/books.png" |absolute_url}})|
|:--:| 
| [Example](https://www.vertabelo.com/blog/chen-erd-notation/) |

以上圖為例，CHAPTER 必須依靠 BOOK 才能存在，所以 CHAPTER 是一個弱實體，兩者間用雙菱形（弱關聯）來連結。CHAPTER 用雙直線（Total participation）連接關係，因為 CHAPTER 是依靠 BOOK 而存在，表示每一個 CHAPTER 必定屬於某本 BOOK。而 CHAPTER 的 primary key 由 BOOK 的 primary key（BOOK ID） 與 CHAPTER ID 組成。

如果將上圖關係轉換成表格，CHAPTER 表格會有 {TITLE, CHAPTER ID, BOOK ID} 三個欄位，而 (CHAPTER ID, BOOK ID) 合併為 primary key。
  


***

**Reference:**
<br>
[ER Model 實體關係圖](http://cc.cust.edu.tw/~ccchen/doc/db_03.pdf)
<br>
[第4章 資料庫設計與實體關聯模型](http://www.csie.sju.edu.tw/cm/course/db/ch04.pdf)
<br>
[利用實體-關係模型 (E-R Model) 規劃資料庫](http://spaces.isu.edu.tw/upload/19225/0/news/postfile_308.pdf)
<br>
[Chen notation](https://www.vertabelo.com/blog/chen-erd-notation/)
<br>
[資料庫基礎概念](http://snowlin.cmu.edu.tw/mis/MIS_Lec01.pdf)
