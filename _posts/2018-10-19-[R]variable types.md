---
layout: post
comments: true
title: "[R]variable types"
date: 2018-10-19 10:32
author: "Shihs"
category: [R]
---

We know there are several common types in R, such as, vector, list, matrix, and data.frame.
<br>
Here I'm going to see these 4 types more details. 

1. What are the differences between vector, list, matrix, and data.frame?
2. What are the outputs of `is.atomic()` and `is.vector()`? 
3. What are the outputs of `typeof()`?

***


### 1. What are the different between *vector*, *list*, *matrix*, and *data.frame*?

We can seperate these four types to two groups from different aspects.

**(a) Elements type aspect**
- Homogeneous data: *vector*, *matrix*
- Heterogeneous data: *list*, *data.frame*

Which means all elements in *vector* and *matrix* have to be the same type (integer, double, or character ect.).
But elements in *list* and *data.frame* can be different types.

For example:
<br>
Vector has same type of elements
```r
# vector
v <- 1:4
#  v
# [1] 1 2 3 4

v_ch <- c("a", "b", "c")
# v_ch
# [1] "a" "b" "c"
```
What if we give a vector different type of elements?
```r
v <- c(1, "2")
# v
#[1] "1" "2"
```
As you can see, R forces 1 to be character.

But what is the priority? Why not "2" become numeric?

Because **the hierarchy for coercion** is:
<br>
- **logical < integer < numeric < character**

So this is why numeric would be force to character.

[reference](https://campus.datacamp.com/courses/introduction-to-r-for-finance/vectors-and-matrices?ex=3)

**(b) Dimension aspect**
- 1 Dimension: *vector*, *list*
- 2 Dimensions: *matrix*, *data.frame*

***

### 2. What are the outputs of `is.atomic()` and `is.vector()`? 

Let's see the outputs of these four types.

```r
v <- 1:4 # vector
l <- list(1:4) # list
mat <- matrix(1:2, ncol = 2) # matrix
df <- data.frame(a = 1, b = 2) # data.frame
```

**(a) is.atomic()**

```r
# > is.atomic(v)
# [1] TRUE
# > is.atomic(l)
# [1] FALSE
# > is.atomic(mat)
# [1] TRUE
# > is.atomic(df)
# [1] FALSE
```
As you can see the results, `is.atomic()` gives boolean values.
<br>
And the output is to see if the object is *Homogeneous data* or *Hetergeneous data*.
<br>
Hence, *vector* and *matrix* get TRUE, *list* and *data.frame* get FALSE.


**(b) is.vector()**

```r
# is.vector(v)
# [1] TRUE
# is.vector(l)
# [1] TRUE
# is.vector(mat)
# [1] FALSE
# is.vector(df)
# [1] FALSE
```
In contrast with is.atomic(), `is.vector()` checks from Dimension aspect.

***

### 3. What are the outputs of `typeof()`

```r
# vector
v <- 1:4  # all elements are numeric
v_ch <- c("a", "b", "c")  # all elements are characters
# list
l <- list(1:4)  # all elements are numeric
l_ch <- list(a = "a", b = "b") # all elements are characters
# matrix
mat <- matrix(1:2, ncol = 2)  # all elements are numeric
mat_ch <- matrix(c("a", "b"), ncol = 2)  # all elements are characters
# data.frame
df <- data.frame(a = 1, b = 2)
```
Let's see the results,
```r
# ---vector-------------
# > typeof(v)
# [1] "integer"
# > typeof(v_ch)
# [1] "character"
# ---list-------------
# > typeof(l)
# [1] "list"
# > typeof(l_ch)
# [1] "list"
# ---matrix-------------
# > typeof(mat)
# [1] "integer"
# > typeof(mat_ch)
# [1] "character"
# ---data.frame-------------
# > typeof(df)
# [1] "list"
```

From the result of ouputs, we can see it checks if the object is *Homogeneous data* or not.
<br>
If it is *Homogeneous data* then `typeof()` will show the type of elements.
<br>
But if the object is *Hetergeneous data*, it will give only *list* as output result.










***

More detail about Data Structure can be found [here](http://adv-r.had.co.nz/Data-structures.html)

Reference:
<br>
[R深入|数据类型](https://zhuanlan.zhihu.com/p/25551827)

