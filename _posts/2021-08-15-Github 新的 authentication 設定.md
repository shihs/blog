---
layout: post
comments: true
title: "Github 新的 authentication 設定"
date: 2021-08-15 15:03
author: "Shihs"
category: []
---

Github 從 8/13 開始將以前的 password 認證方式刪除了，這裡記錄我解決的方法。

- 使用 ssh
- 使用 personal access token

---

### 1. 使用 ssh

情況：

![]({{ "/img/posts/git push.png" |absolute_url}})

- 之前已 clone 下來的 repo
- 修改後要 push 碰到下面的錯誤訊息

```bash=
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: unable to access 'https://github.com/shihs/to-do-list-app.git/': The requested URL returned error: 403
```

**Step 1:** Enabling two-factor authentication

- 根據錯誤訊息提供的[網址](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/)，先去 **Enabling two-factor authentication**，照著 [Configuring two-factor authentication recovery methods](https://docs.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication-recovery-methods) 的步驟做（裡面提到的 TOTP app 我是用 [Salesforce Authenticator](https://www.salesforce.com/solutions/mobile/app-suite/security/)）。

**Step 2:** 加 ssh key

- 確認 github 是否已經加了 ssh key `ssh -t git@github.com`，如果沒加會出現像這樣的訊息![]({{ "/img/posts/ssh test.png" |absolute_url}})
- 在本機 gen ssh key，並在 github 頁面新增 ssh key。我主要是參考下面兩個網址：
  - [Git 版本控制筆記 - 使用 github 及 ssh 金鑰設定](https://blog.jaycetyle.com/2018/02/github-ssh/)
  - [生成新 SSH 密钥并添加到 ssh-agent](https://docs.github.com/cn/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)
- 完成之後在 terminal 打上 `ssh -t git@github.com` 會是
  ![]({{ "/img/posts/ssh success.png" |absolute_url}})

**Step 3:** 重新 push

- `git remote set-url origin git@github.com:[your-github-name]/[repo-name].git`
- 重新 add 和 commit 修改，就可以 push 了

但這樣的方法還是很麻煩......每一支 reop 都要重新 `git remote set-url origin ...` 所以另一個方法是使用 **personal access token**。

**Reference**:
[GitHub Support for password authentication was removed (August 13, 2021) - Solution](https://www.youtube.com/watch?v=5Jz0wVmYUUE)

---

## 2. 使用 personal access token

這裡的方法是在 Mac 的操作。

**Step 1:**

- 參照 github 提供的方法，[Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)。

**Step 2:** 將 create 出來的 token 加到「鑰匙圈」裡

- 使用 spotlight 搜尋「keychain」
- 在 keychain 上搜尋「git」，找到 github
  ![]({{ "/img/posts/keychain.png" |absolute_url}}){:width="70%" heigh="70%"}
- 點選下方「顯示密碼」，並將密碼改成剛剛在 github 上 create 的 token
  ![]({{ "/img/posts/add token.png" |absolute_url}}){:width="70%" heigh="70%"}

現在可以任意地使用之前 clone 下來的 repo 了，不過如果剛剛 create token 有時間限制，之後必須要再重新建立新的密碼並修改。

**Reference**:
[Solved - Support for password authentication was removed - Github - Mac and Windows](https://www.youtube.com/watch?v=aKaYpl-ZpGg)
