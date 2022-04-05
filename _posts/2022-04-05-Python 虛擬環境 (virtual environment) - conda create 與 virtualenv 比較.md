---
layout: post
comments: true
title: "Python 虛擬環境 (virtual environment) - conda create 與 virtualenv 比較"
date: 2022-04-05 13:44
author: "Shihs"
category: [Python]
---


## Virtualenv

`virtualenv`是用來建立一個獨立的`Python`環境的工具，支援 Python2 和 Python3。

1. 安裝 virtualenv：`pip install virtualenv`
2. 建立虛擬環境：
    - 先建立一個資料夾：`mkdir myenv`
    - 路徑移到該資料夾：`cd myenv`
    - 建立虛擬環境：`virtualenv venv`
4. 啟動虛擬環境：`source env/bin/activate`
5. 在該環境下載套件：`pip install PACKAGE_NAME`
6. 停用虛擬環境：`deactivate`

***

## Conda

>Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. It was created for Python programs, but it can package and distribute software for any language.

Conda 是一個開源的跨平台工具軟體，它被設計作為 Python、R、Lua、Scala 與 Java 等任何程式語言的套件、依賴性以及工作環境管理員。傳統 Python 使用者以 pip 作為套件管理員（package manager）、以 venv 作為工作環境管理員（environment manager），而 conda 則達成了「兩個願望、一次滿足」既可以管理套件亦能夠管理工作環境。

### 在 Python 使用 conda
- 可以下載 `Anaconda`（3 GB 以上）或 `Miniconda`（400 MB 左右）
    - `Miniconda` installer = Python + conda
    - `Anaconda` installer = Python + conda + meta package anaconda = `Miniconda` installer + conda install anaconda

**[What are the differences between Conda and Anaconda?](https://stackoverflow.com/questions/30034840/what-are-the-differences-between-conda-and-anaconda/30057885#30057885)**
- `conda` is the package manager. `Anaconda` is a set of about a hundred packages including conda, numpy, scipy, ipython notebook, and so on.
- `Miniconda` is a smaller alternative to Anaconda that is just conda and its dependencies, not those listed above.
- Once you have Miniconda, you can easily install Anaconda into it with `conda install anaconda`.

### 下載
- 下載 [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- 下載 [Anaconda](https://www.anaconda.com/products/individual)



### Cheatsheet
- [Document](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)


**conda 的資訊**
- `conda --version`：檢視 conda 版本
- `conda update conda`：更新 conda 版本
- `conda env list`：conda 所有的環境

**conda basic**
- `conda install PACKAGENAME`：Install a package included in Anaconda
- `conda update PACKAGENAME`：Update any installed program

**環境**
- `conda create --name ENV_NAME python=VERSION`：建立特定版本，名稱為`ENV_NAME`的環境
    - Ex. `conda create --name myenv python=3.6`
- `conda activate ENVIRONMENT`：切換至指定工作環境
- `conda deactivate`：回到 base 工作環境
- `conda list`：active 環境中的所有套件
    - [`Build Channel`](https://stackoverflow.com/questions/62412898/what-does-pypi-in-the-channel-column-of-conda-list-output-imply)的`pypi`表示是用`pip install PACKAGENAME`
    - `pip freeze`可以看到所有用`pip install`下載的套件
![](https://i.imgur.com/yvuy4kT.png)
- `conda env remove --name ENV_NAME`：刪除名稱為`ENV_NAME`的環境



***

**Reference**:
- [輕鬆學習 Python：conda 的核心功能](https://medium.com/datainpoint/python-essentials-conda-quickstart-1f1e9ecd1025)
- [Python — Virtualenv虛擬環境安裝](https://medium.com/python4u/python-virtualenv虛擬環境安裝-9d6be2d45db9)