---
layout: post
comments: true
title: "[Database]Database 基礎概念"
date: 2019-12-31 12:22
author: "Shihs"
category: [Database]
---


## 資料(Data)與資訊(Information)

- 資料(Data)：資訊(Information)的原始型態，是未經整理和分析的原始數值、文字或符號。
- 資訊(Information)：經過整理和分析後的資料，是有實質意義的資料。
- 資料處理(Data Processing)：資料(Data) 經過資料處理(Data Processing) 後將資料轉換為資訊(Information)。

## 資料階層

資料階層的最小儲存單位是位元，8個位元組成一個位元組，也就是ASCII碼的字元。數個位元組結合成欄位，多個欄位組成記錄，最後將一組記錄儲存成檔案，資料庫就是 一組相關檔案的集合。


|![資料階層.png]({{ "/img/posts/資料階層.png" |absolute_url}})|
|:--:| 
| [資料階層](http://www.csie.sju.edu.tw/cm/course/db/ch01.pdf) |

- 第一階層：位元(Bits)
- 第二階層：位元組(Bytes)
- 第三階層：欄位(Fields)
- 第四階層：記錄(Records)
- 第五階層：檔案(Files)
- 第六階層：資料庫(Database)

***

## 資料庫系統(Database System)

資料庫系統(Database System)是由「資料庫」(Database)和「資料庫管理系統」(Database Management System，DBMS)所組成。

|![Database System.png]({{ "/img/posts/Database System.png" |absolute_url}})|
|:--:| 
| [資料庫系統](http://www.csie.sju.edu.tw/cm/course/db/ch01.pdf) |


### 資料庫(Database)
1. Represents some aspects of the real world (miniworld)
2. 資料庫是一個對結構化資訊或資料的組織性收集，通常以電子方式儲存在電腦系統。
3. 資料庫通常由資料庫管理系統(DBMS)控制。
4. 目前運行中最常見的資料庫型態通常是在一系列的表格中進行行列間建模，使得處理和資料查詢更為有效。
5. 大部分的資料庫使用結構化查詢語言(SQL)來書寫或查詢資料。
6. 資料庫容許多名用戶在同一時間快速、安全地以高度複雜邏輯和語言取得或查詢資料。
7. Meta-data: Database definition or descriptive information (Stored by the DBMS in a database catalog or data dictionary)


### 資料庫管理系統(DBMS)
1. 資料庫通常需要一個稱做資料庫管理系統(DBMS)的全面資料庫軟體程式。
2. DBMS是作為資料庫和其用戶或程式之間的介面，讓用戶能檢索、更新和管理，使得資訊組織化和最佳化。
3. DBMS亦可促進對資料庫的監督和控制，增強各方面的管理運作，包括績效監控、最佳化、備份以及系統恢復。

***

## Database System Design Process

好的資料庫系統設計對於資料庫的維護、更新及修改相當重要，另外，如何有效的儲存、提取資料也是資料庫重要的一環，接下來要介紹資料庫的設計。


**資料庫系統設計（Database System Process）**有兩個主要的方向，

1. **Database design**（資料庫設計）
- focuses on defining the database
2. **Application design**（應用設計）
- focuses on the programs and interfaces that access the database

|![Database System Design Process.png]({{ "/img/posts/Database System Design Process.png" |absolute_url}})|
|:--:| 
| [Database System Design Process](https://www.ida.liu.se/~TDDD37/fo/DBTechnology01-2019-6up.pdf) |

***

## Database Design（資料庫設計）/ Data Modeling（資料塑模）

(在 [Database Technology](https://www.ida.liu.se/~TDDD37/fo/DBTechnology01-2019-6up.pdf) 講義裡寫的是 Database Design，但找到兩個台灣的講義（[第1章 資料庫的基礎](http://www.csie.sju.edu.tw/cm/course/db/ch01.pdf)、[第二章 實體關係模式:基本概念](https://www.mis.nsysu.edu.tw/db-book/PDF/Ch2.pdf)）都是用資料塑模（Data Modeling），所以這兩個東西我把它們放在一起)

|![Data Modeling.png]({{ "/img/posts/Data Modeling.png" |absolute_url}})|
|:--:| 
| [Data Modeling](http://www.csie.sju.edu.tw/cm/course/db/ch01.pdf) |



### 資料庫設計階段（Phases for designing a database）:
1. Requirements specification and analysis 
2. **Conceptual design**（Conceptual model，概念塑模)
- e.g., using the Entity-Relationship model (ER Model)
3. **Logical design**（Logical model，邏輯塑模)
- e.g., using the relational model (關聯模型)
4. **Physical design**（Physical model，實體塑模)
- e.g., 設定索引

|![Database development life cycle](https://www.guru99.com/images/DatabaseDesignProcess(1).png)|
|:--:| 
| [Database development life cycle](https://www.guru99.com/database-design.html) |


***

## Conceptual model（概念塑模）

概念塑模的目的是將現實中某部分的資料關係用**結構化**的方式呈現，建立整個資料庫邏輯結構的模型，過程不涉及任何資料庫管理系統、資料庫種類、軟體和實際儲存結構。最常使用*實體關係圖*（Entity Relationship Diagram）來繪製*實體關聯模型*（Entity-Relationship Model）。

|![ER Model.png]({{ "/img/posts/ER Model.png" |absolute_url}})|
|:--:| 
| [ER Model](http://www.csie.sju.edu.tw/cm/course/db/ch03.pdf) |


### Entity-Relationship model (ER Model)

1. ER Model 則是用來繪製**結構化**資料的概念圖。
2. ER Model 組成元件包括實體（Entity）和關係（Relationship）。
- 實體（Entity）- 是在真實世界識別出的東西，例如：老師、學生、車子、品牌。
- 關聯性（Relationships）- 在二個或多個實體間擁有的關係，主要分為三種：一對一、一對多、多對多。

[下一篇](https://shihs.github.io/blog/database/2020/01/01/Database-ER-Model實體關係圖/)有詳細解說

***

## Logical model（邏輯塑模）

使用的工具是關聯模型（Relational Model），最後會產生資料表的定義關聯綱目（schema）。

邏輯模型主要是由三種元素所組成，如下所示:
- 資料結構（Data Structures）：資料的組成方式，就是欄和列組成表格的關聯表(Relations)
- 資料操作或運算（Data Manipulation 或 Operations）：資料的相關操作，關聯式代數(Relational Algebra)和關聯式計算(Relational Calculus)
- 完整性限制條件（Integrity Constraints）：維護資料完整性的條件，其目的是確保儲存的資料是合法的資料

資料庫系統演進各年代的資料庫系統中，其使用的資料庫模型就是邏輯資料模型，主要有四種邏輯資料模型，如下所示:
- 階層式模型（Hierarchical Model）
- 網路式模型（Network Model）
- **關聯式模型（Relational Model）**[wiki]((https://zh.wikipedia.org/wiki/关系模型))
- 物件導向式模型（Object-Oriented Model）


### Relational Model (Relational Data Model)

- 中文稱「關聯（式）模型」。
- Relational database 關聯式資料庫: represent data as a collection of relations。「關聯式資料庫」使用多個關聯表（relations）來呈現資料。

**Relation（關聯表）**

|![relation.png]({{ "/img/posts/relation.png" |absolute_url}})|
|:--:| 
| [relation (關聯表)](https://www.ida.liu.se/~TDDD37/fo/DBTechnology02-2019-6up.pdf) |

- Relation 是關聯表（如上圖），是包含 data 的 table（表格）

- Each row (tuple) represents a record of related data values 
  - 一列（row）稱為一個值組（tuple），紀錄各個 data 的值

- Each column (attribute) holds a corresponding value for each row
  - Columns associated with a data type (domain)
  - Each column header: attribute name

- **Domain**
  - Domain is a set of *atomic values*. 
    <br>
    e.g., $$\{ 0, 1, 2, ... \}$$, $$\{\text{Jo Smith}, \text{Dana Jones}, \text{Ashley Wong}, \text{Y. K. Lee}, ...\}$$
  - *atomic values*: Each value indivisible（不可分割）
  - Domains specified by *data type*(integer, string, date, real, etc.)

- **Relation Schema** 
  - Schema describes the relation（關聯表）
  - 關聯表綱要（relation schema）是由關聯表名稱 R（relation name）和一連串屬性 $$(A_1,A_2,….,A_n)$$清單（list）還有定義域（domain）所組成
  - **integrity constraints**（完整性限制）
  - Denoted by $$R(A_1, A_2, ..., A_n)$$

- **Attribute** $$A_i$$
  - Name of a role in the relation schema R
  - 使用 $$dom(A_i)$$ 的符號來說明屬性 $$A_i$$ 的定義域的範圍是什麼
  - 屬性名稱不可重複，但 domain 可以重複

- **NULL Values**
  - Each domain may be augmented with a special value called NULL

- *Question:* A relation schema consists of? 
  - Ans: relation name, attribute names and domains, and integrity constraints
 

### Integrity Constraints（完整性限制）

- 建立檢查資料庫儲存資料的依據和保障資料的正確性。不但可以防止授權使用者將不合法資料存入資料庫，還能夠避免關聯表間的資料不一致。
- 關聯式資料庫模型的完整性限制條件有很多種，適用所有關聯式資料庫的完整性限制條件有四種，如下所示:
  - 鍵限制條件(Key Constraints)
  - 定義域限制條件(Domain Constraints)
  - 實體完整性(Entity Integrity)
  - 參考完整性(Referential Integrity)


**鍵限制條件（Key Constraints）**

鍵限制條件（Key Constraints）是指關聯表一定擁有一個唯一和最小的主鍵（Primary Key）

|![keys.png]({{ "/img/posts/keys.png" |absolute_url}})|
|:--:| 
| [Key](http://www.csie.sju.edu.tw/cm/course/db/ch03.pdf) |


- 超鍵（Superkeys）
  - 是關聯表綱要的單一屬性或屬性值集合，超鍵需要滿足唯一性（Uniqueness）
  - Superkeys 可以由一個或多個行（屬性）組成，只要唯一就可以
  - 下方範例關聯表來看，符合的有(sid)、(SSN)、(sid, SSN)、(sid, ename)、(SSN, cname)、(sid, tel)、(SSN, cname, postcode)......

- 候選鍵（Candidate Keys）
  - 候選鍵(Candidate Keys)是一個超鍵，在每一個關聯表至少擁有一個候選鍵，不只滿足超鍵的唯一性，還需要滿足最小性（Minimality）
  - Candidate Keys 是超鍵的子集合，但不同的是，候選鍵還必須要有最小性，所以單一屬性的超鍵一定是候選鍵
  - 舉個例子，如果下面的範例多了一個學生 sid = 5, ename = Jane，這時候 (sid, ename) 就不是候選鍵，因為去掉 ename 也能區分每一行，所以 ename 是多餘的

- 主鍵（Primary Key）
  - 符合的有(sid)、(SSN)
  - 從候選鍵中選出一個作為主鍵，挑選主鍵的原則如下所示:
    - 不可為空值(Not Null)
    - 永遠不會改變(Never Change)
    - 非識別值(Nonidentifying Value)
    - 簡短且簡單的值(Brevity and Simplicity)

- 替代鍵（Alternate Keys）
  - 在候選鍵中不是主鍵的其他候選鍵稱為替代鍵(Alternate Keys)，因為這些是可以用來替代主鍵的候選鍵
  - 如果 (sid) 是主鍵，則 (SSN) 是替代鍵

- 外來鍵（Foreign Keys）
  - 是關聯表的單一或多個屬性的集合，它的屬性值是參考到其他關聯表的主鍵，用來建立兩個關聯表間的連接
  - 換句話說，Foreign Keys 是其他關聯表的主鍵，它（們）可以是該關聯表的主鍵，但不一定是
  - 外來鍵和參考的主鍵屬於相同定義域，不過屬性名稱可以不同
  - 外來鍵可以是空值NULL
  

|![Students.png]({{ "/img/posts/Students.png" |absolute_url}})|
|:--:| 
| [範例關聯表](http://www.csie.sju.edu.tw/cm/course/db/ch03.pdf) |


**定義域限制條件(Domain Constraints)**
- 每個值都必須是基元值且必須在定義域內
- 例如，屬性 age 的定義域是 int，屬性值可以為5 ，但不可以是4.5


**實體完整性(Entity Integrity)**
- 實體完整性是關聯表內部的完整性條件，主要是用來規範關聯表主鍵的使用規則
- 主鍵（primary  key）不可以是 Null
- 例如，（ename, cname）是主鍵，ename 屬性不可為空值；cname 屬性也不可是空值。


**參考完整性(Referential Integrity)**
  - 關聯表的所有外來鍵值，都必須能參考到另一關聯表的主鍵值




***

## Physical Model（實體塑模）

- 針對指定資料庫管理系統建立實際資料庫結構的資料模型，例如:SQL Server
- 對於關聯式資料庫模型的實體模型來說，就是在資料庫管理系統軟體建立關聯表(Relation) 的表格、關聯性(Relationship)和索引等定義資料
- 簡單來說，就是將 Conceptual model 和 Logical model 實際建立出來

|![實體模型.png]({{ "/img/posts/實體模型.png" |absolute_url}})|
|:--:| 
| [實體模型](http://www.csie.sju.edu.tw/cm/course/db/ch03.pdf) |







***

**Reference:**
<br>
[第1章 資料庫的基礎](http://www.csie.sju.edu.tw/cm/course/db/ch01.pdf)
<br>
[第3章 關聯式資料庫模型](http://www.csie.sju.edu.tw/cm/course/db/ch03.pdf)
<br>
[Oracle - 什麼是資料庫？](https://www.oracle.com/tw/database/what-is-database.html)
<br>
[Database Technology - Topic 1: Introduction](https://www.ida.liu.se/~TDDD37/fo/DBTechnology01-2019-6up.pdf)
<br>
[Database Technology - Topic 2: Relational Databases](https://www.ida.liu.se/~TDDD37/fo/DBTechnology02-2019-6up.pdf)
<br>
[深入了解關聯式資料模型(Relational Data Model)](http://championdatablog.com/自動草稿/)
<br>
[第二章 實體關係模式:基本概念](https://www.mis.nsysu.edu.tw/db-book/PDF/Ch2.pdf)
<br>
[Data Modeling (資料塑模) : 概念塑模、邏輯塑模、實體塑模](https://www.mysql.tw/2015/04/data-modeling.html)
<br>
[快速理解資料庫超鍵，候選鍵，主鍵](https://www.itread01.com/content/1545320464.html)



