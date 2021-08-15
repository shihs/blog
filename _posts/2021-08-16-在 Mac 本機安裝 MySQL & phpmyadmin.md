---
layout: post
comments: true
title: "在 Mac 本機安裝 MySQL & phpmyadmin"
date: 2021-08-16 01:34
author: "Shihs"
category: []
---

#### 1. 啟動 Apache

-   `sudo apachectl start`
-   打開瀏覽器 http://localhost/ 可以看到 **It works!**

#### 2. 下載 MySQL

-   https://dev.mysql.com/downloads/mysql/
-   選擇下載 `.dmg` 檔
-   下載完後安裝，安裝過程需要**設定 root 的密碼**
-   打開系統偏好設定會看到出現 MySQL 的圖示，點選後啟動 MySQL
    ![](https://i.imgur.com/tusQ0GN.png){:width="70%" heigh="70%"}
    ![](https://i.imgur.com/rpAQ8yJ.png){:width="70%" heigh="70%"}

#### 3. 使用 terminal 開啟 MySQL

-   `mysql -u root -p`（`-u`: user, `-p`: password）
-   出現 `Enter password:` 後輸入剛剛安裝時設定的 root 密碼
    ![](https://i.imgur.com/dsXdFmP.png){:width="70%" heigh="70%"}

#### 4. 下載 phpmyadmin

這個步驟不是必須，下載 phpmyadmin 是為了可以使用操作介面查看 MySQL。

-   下載：https://www.phpmyadmin.net/downloads/
-   瀏覽器打開 http://localhost/phpmyadmin/index.php
    ![](https://i.imgur.com/orDEaCz.png){:width="70%" heigh="70%"}

#### 5. 設定 phpmyadmin 登入密碼

因為 phpmyadmin 的密碼身份驗證是 `caching_sha2_password` 所以會無法使用一開始設定的 root 與密碼登入，這時候需要先修改 db 的資料。

-   terminal 登入 MySQL（[step 3](https://hackmd.io/xwgJ-FoRSsSVk6WCrgRXlA?view#3-%E4%BD%BF%E7%94%A8-terminal-%E9%96%8B%E5%95%9F-MySQL)）
-   將 root 的密碼身份驗證由 `caching_sha2_password` 改成 `mysql_native_password`
    -   `use mysql；`（使用 `mysql` 這個 db）
    -   `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的密碼';`
    -   `FLUSH PRIVILEGES;`
-   這時候 phpmyadmin 就可以使用設定好的 root 的密碼登入了

---

### 新增新的 MySQL User

通常不會讓所有人都使用 root 權限操作 db，這時候就需要增加新的 user 讓其他人使用。

-   terminal 登入 MySQL（[step 3](https://hackmd.io/xwgJ-FoRSsSVk6WCrgRXlA?view#3-%E4%BD%BF%E7%94%A8-terminal-%E9%96%8B%E5%95%9F-MySQL)）
-   新增 User
    -   `use mysql；`
    -   `CREATE USER 'USERNAME'@'localhost' IDENTIFIED BY 'PASSWORD';`
    -   `ALTER USER 'username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';`
    -   `FLUSH PRIVILEGES;`
-   設定完成後 phpmyadmin 和 terminal 都可以使用設定好的帳號密碼登入
    -   `mysql -u USERNAME -p` / `PASSWORD`

#### 設定新增 User 的權限

-   查看某 user 的權限：
    `SHOW GRANTS FOR 'username'@'localhost';`
-   GRANT 權限：
    `GRANT type_of_permission ON database_name.table_name TO 'username'@'localhost';`
-   REVOKE 權限：
    `REVOKE type_of_permission ON database_name.table_name FROM 'username'@'localhost';`
-   reload all the privileges：`FLUSH PRIVILEGES;`

---

**Reference**

-   [Mac 電腦執行 PHP & MySQL & phpMyadmin](https://jqnets.com/blog/mac-%E9%9B%BB%E8%85%A6%E5%9F%B7%E8%A1%8C-php-mysql-phpmyadmin/)
-   [phpmyadmin 連線 MySQL8.0 報錯#2054 - The server requested authentication method unknown to the client](https://www.itread01.com/content/1546243084.html)
-   [How To Create New MySQL User and Grant Privileges](https://phoenixnap.com/kb/how-to-create-new-mysql-user-account-grant-privileges)
-   [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
