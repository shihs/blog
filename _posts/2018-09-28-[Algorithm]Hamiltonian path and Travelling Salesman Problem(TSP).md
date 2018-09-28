---
layout: post
comments: true
title: "[Algorithm]Hamiltonian path and Travelling Salesman Problem(TSP)"
date: 2018-09-28 10:36
author: "Shihs"
category: [Algorithm]
---

以下簡單地整理網路上查到的 Hamiltonian path 與 Travelling Salesman Problem 介紹。

***

### Hamiltonian path

**What is Hamiltonian path?**<br>
[Hamiltonian path](https://en.wikipedia.org/wiki/Hamiltonian_path) is a path that visit every node only once. It can be an undirected or directed graph. Also it

**Hamiltonian cycle**<br>
If a Hamiltonian path is a cycle then we call it A Hamiltonian cycle (or Hamiltonian circuit).

**Hamiltonian path problem**<br>
Determining whether such paths and cycles exist in graphs is the Hamiltonian path problem, which is NP-complete

***

### Travelling Salesman Problem

**What is Travelling Salesman Problem(TSP)?**<br>
There is a man traveling. He departures from a city and he wants to visit every cities(nods) with the shortest distance. In the end, he will go back to the origin city, and he can only stop in each city once. 

Which means, TSP is looking for the shortest distance of *Hamiltonian cycle*.

***

reference:<br>
[演算法筆記](http://www.csie.ntnu.edu.tw/~u91029/Circuit.html)<br>
[Wikipedia - TSP](https://en.wikipedia.org/wiki/Travelling_salesman_problem)<br>
[Wikipedia - Hamiltonian path](https://en.wikipedia.org/wiki/Hamiltonian_path)<br>