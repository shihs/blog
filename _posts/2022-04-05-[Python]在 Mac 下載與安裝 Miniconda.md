---
layout: post
comments: true
title: "[Python]在 Mac 下載與安裝 Miniconda"
date: 2022-04-05 17:41
author: "Shihs"
category: [Python]
---

Conda 是除了能夠管理套件也能夠管理工作環境，是個好用的工具。
之前是下載 Anaconda 來使用 Conda，但 Anaconda 在最一開始下載時就會下載很多套件，可是大多數的套件其實都用不到，卻又佔用了大量的空間（Anaconda 在刪除前我在的電腦佔用了十幾 GB），因此決定轉換使用 Miniconda 來使用 conda。



## 刪除 Anaconda

參考官網的 [uninstall Anaconda](https://docs.anaconda.com/anaconda/install/uninstall/) 的方法。

原本想使用第二種方法 `conda install anaconda-clean`，但在下載 `anaconda-clean` 時一直碰到問題，所以最後決定使用第一種方法。

直接刪除整個 `rm -rf ~/anaconda3` 資料夾，為避免這種刪法沒有刪乾淨，再手動搜尋 `anaconda` 刪除所有相關的檔案。



## 下載與安裝 Miniconda

1. 到官網下載 [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
    - 根據步驟一直點選下一步就好
2. 安裝完成後，Miniconda 會自動在 `.zchrc` 和 `.bash_profile` 加上路徑
    ```bash
    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/Users/your_user_name/opt/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/Users/your_user_name/opt/miniconda3/etc/profile.d/conda.sh" ]; then
            . "/Users/your_user_name/opt/miniconda3/etc/profile.d/conda.sh"
        else
            export PATH="/Users/your_user_name/opt/miniconda3/bin:$PATH"
        fi
    fi
    unset __conda_setup
    # <<< conda initialize <<<
    ```
3. 確認是否安裝成功
    - 打開 terminal，`conda --version` 如果能正確顯示 conda 版本，就表示 conda 順利安裝完成！

## conda 常用指令

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
![](https://i.imgur.com/gnlRU35.png)
- `conda env remove --name ENV_NAME`：刪除名稱為`ENV_NAME`的環境