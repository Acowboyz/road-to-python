# Python Databases Notes
<br>

## 目錄
* **[MySQL](#MySQL)**
    * [資料庫簡介](#資料庫簡介)
    * [關聯性資料庫](#關聯性資料庫-relational-database)
    * [安裝與管理](#安裝與管理)
    * [資料庫的相關操作](#資料庫的相關操作)
    * [查詢](#查詢)
    * [進階用法](#進階用法)
* **[MongoDB](#MongoDB)**
    * [NoSQL 簡介](#)

<br><br>
## MySQL

<br><br>
### 資料庫簡介

<br>

[資料庫排名](https://db-engines.com/en/ranking)

當前使用資料庫主要的分列為兩類
* 文檔型
    * 如 sqlite ，透過對文件的複製完成資料庫的複製
* 服務型
    * 如 mysql, postgresql ，資料儲存在一個物理文件，需要使用 tcp/ip 的協議進行數據庫的讀寫操作

<br>

#### E-R 模型

當前物理的資料庫都是按照 E (entry)-R (relationship) 模型進行設計
* 實體轉換為資料庫的表
* 關係則描述兩個實體間的對應規則
    * 一對一
    * 一對多
    * 多對多

<br>

#### 三正規化 


* [第一正規化 (First Normal Form, 3NF)](https://zh.wikipedia.org/wiki/%E7%AC%AC%E4%B8%80%E6%AD%A3%E8%A6%8F%E5%8C%96)
    * 為了排除**重複群**的出現，所採用的方法是要求資料庫的每個列的值都是由原子值組成，並且每個欄位的值都只能是單一值
* [第二正規化 (Second Normal Form, 3NF)](https://zh.wikipedia.org/wiki/%E7%AC%AC%E4%BA%8C%E6%AD%A3%E8%A6%8F%E5%8C%96)
    * 要求資料表裡的所有資料都要和該資料表的鍵（主鍵與候選鍵）有完全依賴關係
    * 每個非鍵屬性必須獨立於任意一個候選鍵的任意一部分屬性
* [第三正規化 (Third Normal Form, 3NF)](https://zh.wikipedia.org/wiki/%E7%AC%AC%E4%B8%89%E6%AD%A3%E8%A6%8F%E5%8C%96)
    * 要求所有非鍵屬性都只和候選鍵有相關性
    
每一個正規化都是在前一個正規化基礎上建立


<br><br>

### 關聯性資料庫 (relational database)

<br>

[WIKI 簡介](https://zh.wikipedia.org/wiki/%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE%E5%BA%93)
[AWS RDS](https://aws.amazon.com/tw/relational-database/)

<br><br>
### 安裝與管理

<br>

#### 安裝

```bash
sudo apt-get install mysql-server mysql-client
```

<br>

#### 管理服務

啟動
```bash
service mysql start
```

停止
```bash
service mysql stop
```

重新啟動
```bash
service mysql restart
```

<br>

#### 設定

[MySQL 設定檔位置](https://stackoverflow.com/questions/2482234/how-do-i-find-the-mysql-my-cnf-location)
[修正無法登入問題](https://superuser.com/questions/603026/mysql-how-to-fix-access-denied-for-user-rootlocalhost)

<br><br>

### 資料庫的相關操作

<br>

#### 連接資料庫

登入
```bash
mysql -uroot -p
```

退出
```bash
quit
```

查看版本

```mysql
mysql> select version();
+-------------------------+
| version()               |
+-------------------------+
| 5.7.22-0ubuntu0.16.04.1 |
+-------------------------+
1 row in set (0.00 sec)
```

顯示時間

```mysql
mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2018-06-15 20:21:56 |
+---------------------+
1 row in set (0.00 sec)
```


#### 資料庫基本操作

查看資料庫
```mysql
show databases;
```


創建資料庫
```mysql
create database databasename charset=utf8mb4;
```

刪除資料庫
```mysql
drop database databasename;
```

切換資料庫
```mysql
use databasename;
```

查看當前選擇的資料庫
```mysql
select database();
```

> Hint
>
> [使用 utf8mb4 代替 utf8](https://medium.com/@adamhooper/in-mysql-never-use-utf8-use-utf8mb4-11761243e434)
<br>

#### 資料庫的表操作

查看當前資料庫的所有表
```mysql
show tables;
```

創建表
```mysql
create table students(
id int auto_increment primary key,
stuname varchar(10) not null
);
```

修改表
```mysql
alter table tablename add|change|drop columnname type;
alter table students add birthday datetime;
```

刪除表
```mysql
drop table tablename;
```

查看表結構
```mysql
desc tablename;
```

更改表名稱
```msql
rename table oldtablename to newtablename;
```

查看表創建時的語法
```mysql
show create table tablename;
```

<br>

#### 資料操作

查詢
```mysql
select * from tablename;
```

增加
```mysql
全列插入
insert into tablename values(...);

默認插入
insert into tablename(col1,...) values(val1, ...);

同時插入多條資料
insert into tablename values(...),(...);
insert into tablename(col1, ...) values(val1, ...),(val2, ...),
```

修改
```mysql
update tablename set col1 =val1, ... where condition
```

刪除
```mysql
delete from tablename where condition
```

邏輯刪除
```mysql
alter table tablename add isdelete bit default 0;
update tablename set isdelete=1 where ...;
```

<br>

#### 備份與恢復

資料備份

```bash
sudo -s
cd /var/lib/mysql
mysqldump -uroot -p databasename > ~/backupname.sql;
```

資料恢復
* 創建資料庫
* 恢復備份

```bash
mysql -uroot -p databasename < ~/backupname.sql
```

<br><br>

### 查詢

<br>

#### 條件

```mysql
select * from tablename where condition;
```

<br>

比較運算符

| 符號   | 意義   |
| :---: | :---: |
| =     | 等於   
| >     | 大於   
| >=    | 大於等於  
| <     | 小於
| <=    | 小於等於
| !=    | 不等於
| <>    | 不等於

```mysql
select * from tablename where id>3;
``` 

```mysql
select * from tablename where sname!='felix';
```

```mysql
select * from tablename where isdelete=0;
```

<br>

邏輯運算符

* and
* or
* not

```mysql
select * from tablename where id>3 and gender=0;
```

<br>

模糊查詢

* like
    * % 表示多個任意字元
    * _ 表示一個任意字元

```mysql
select * from tablename where sname like 'f%'
```

<br>

範圍查詢

* in 表示在一個非連續的範圍
* between 表示在一個連續範圍


```mysql
select * from tablename where id in(1,3,8);
```

```mysql
select * from tablename where id between 3 and 8;
```

<br>

判斷是否為空

* is null
* is not null

```mysql
select * from tablename where isdelete is null;
```

<br>

優先級


<br>

#### 聚合函數

* 為了快速得到統計資料

計算總數
count(*)
```mysql
select count(*) from tablename;
```

求此列的最大值
max(*)
```mysql
select max(id) from tablename where gender=0;
```

求此列最小值
min(*)
```mysql
select min(id) from tablename where gender=1;
```

求此列和
sum(*)
```mysql
select sum(id) from tablename where gender=0;
```

求此列平均
avg(*)
```mysql
select avg(id) from tablename where gender=1;
```

<br>

#### 分組

```mysql
select col1, col2, count(*) ... from tablename group by col1, col2 ...
```

查詢男女總數
```
select gender as g, count(*) from tablename group by gender;
```


分組後的數據篩選

```mysql
select col1, col2, aggregation(*) ... from tablename 
group by col1, col2 
having col1
```

```mysql
select count(*) from tablename where gender=1;

select gender, count(*) from tablename group by gender having gender=1;
```

* where 是對原始資料的篩選
* having 是對分組後的資料篩選

<br>

#### 排序

對資料進行排序

```mysql
select * from tablename
order by col1 asc|desc, col2 asc|desc;
```

* 默認從小到大排列
* asc 從小到大排列
* desc 從大到小排列

```mysql
select * from tablename
where gender=1 and isdelete=0
order by id desc
``` 

```mysql
select * from tablename
where isdelete=0
order by title;
```
<br>

#### 分頁

獲取部份行

* 當資料量過大時，需要分批查看資料
* 從 start 開始，獲取 count 條資料

```mysql
select * from tablename
limit start, count
```

* 每頁顯示 m 條資料，當前顯示第 n 頁

```mysql
select * from tablename
where isdelete=0
limit (n-1)*m, m
```

<br><br>

### 進階用法

<br>


<br><br>

## MongoDB

<br><br>

### MongoDB 簡介

<br>


<br><br>

### NoSQL 簡介

<br>




