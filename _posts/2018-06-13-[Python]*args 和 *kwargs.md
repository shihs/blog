---
layout: post
comments: true
title: "[Python]Python 中的 *args 和 *kwargs"
date: 2018-06-13 12:48
author: "Shihs"
category: [Python]


---

簡單來說，`*args`和`**kwargs`是 function 的參數，在不確定會有多少參數時使用。<br>
args 是 arguments 縮寫，kwargs 是 keyword argments 的縮寫。也就是， args 是沒有 keyword 的變數， kwargs 有 keyword。<br>
如果 `*args`和`**kwargs` 同時使用，**`*args`必需在`**kwargs`之前**。

先簡單看以下的例子
```python
def test(*args, **kwargs):
    for i in args:
        print "agrs=" + str(i)

    for j in kwargs:
        print "kwargs=" + j
		
test(1, 2, 3, 4, first = "a", second = "b", third = "c")
```
結果
```
agrs=1
agrs=2
agrs=3
agrs=4
kwargs=second
kwargs=third
kwargs=first
```

<br>

### args 和 kwargs 不是重點，* 才是

args 和 kwargs 這兩個參數名稱並不是重點，重點是前面的星號 `*`。<br>
所以，if you like 其實參數也可以寫成 `*var` 和 `**vars`，`*args` 和 `**kwargs` 只是一個大家使用的習慣。



### *args 的用法

```python
first_arg = "this is first arguments"

def arg_test(first_arg, *args):
    print "first_arg=" + first_arg

    if args is not None:
        print "other *args..."
        for i in args:
            print "agrs=" + str(i)

    arg_test(first_arg, 1, 2, 3, 4)

```
結果
```
first_arg=this is first arguments
other *args...
agrs=1
agrs=2
agrs=3
agrs=4
```


### *kwargs 的用法
```python
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)
 
greet_me(name="yasoob")
```
```
name == yasoob
```
從以上兩個範例可以看出 args 和 kwargs 用法的差異。





### 使用 list 和 dictionary 當參數
```python

def test_arg(arg1, arg2, arg3):
    print arg1
    print arg2
    print arg3


#===args===========
args = [1, 2, 3]
test_arg(*args)

# result
arg1=1
arg2=2
arg3=3

#===kwargs===========
kwargs = {
    "arg3":1,
    "arg2":2,
    "arg1":3
}

test_arg(**kwargs)

# result
arg1=3
arg2=2
arg3=1
```

根據以上範例，可以發現`*arg` print 的順序就是 list 的順序，但 `**kwargs` 會根據 dictionary 的 key 來賦予 value。



<br>


[參考](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)


