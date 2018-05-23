# Python Basic
<br>

## 目錄
* **[初遇 Python](#初遇-python)** 
    * [Hello Python](#hello-python)
    * [變量與類型](#變量與類型)
    * [命名規則與關鍵字](#命名規則與關鍵字)
    * [輸出](#輸出)
    * [輸入](#輸入)
    * [運算符號](#運算符號)
    * [數據類型的轉換](#數據類型的轉換)
    * [比較運算符號](#比較運算符號)
* **[判斷與循環](#判斷與循環)**
    *

<br><br>
## 初遇 Python
<br>

Python 之父 [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) ，荷蘭人，出生於 1982 年。

[Life is short, you need Python](http://sebsauvage.net/python/) - Bruce Eckel

#### 小知識

* Python 誕生於 1991 年
* Python 的意思為蟒蛇，源於作者喜歡的一部電視劇
* Python 的解釋器由多個語言實現
    * Cpython (官方版本)
    * Jython ( java 平台)
    * IronPython ( .NET 和 Mono 平台)
    * PyPy (Python 由 Python 實現，支援 [JIT](https://en.wikipedia.org/wiki/Just-in-time_compilation) )
* 2018 的[程式語言排行榜](https://www.tiobe.com/tiobe-index/) Python 位於第四名

<br><br>

### Hello Python
<br>

第一個 Python 的程式碼

```python
print("Hello Python!")
```

<br><br>

### 變量與類型
<br>

變量為用來儲存數據

```python
# define a variable
num = 100
```

變量的類型

* Numbers
    * int
    * long
    * float
    * complex
* Boolean
    * True
    * False
* String
* List
* Tuple
* Dictonary
* Set    

> Hint : 可以使用 `type()` 來查看變量的類型

<br><br>

### 命名規則與關鍵字
<br>

命名規則需遵守 [PEP8](https://www.python.org/dev/peps/pep-0008/)

Python 有一些具有特殊功能的關鍵字，不允許開發者重複定義與關鍵字相同名字

查看關鍵字

```python
Python 3.5.4 |Anaconda custom (64-bit)| (default, Nov 20 2017, 18:44:38) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
 'return', 'try', 'while', 'with', 'yield']
```

<br><br>

### 輸出
<br>

輸出格式

```python
age = 18
name = "Felix"
print("My name is %s \n, Age is %d"%(name, age))
```

常用的格式符號

| 符號   | 意義 
| :---: | :---:  
| %c    | 字符
| %s    | 通過 `str()` 轉換
| %i    | 十進制整數
| %d    | 十進制整數
| %u    | 無正負十進制整數
| %o    | 八進制整數
| %x    | 十六進制整數
| %e    | Exponent notation
| %f    | 浮點數
| %g    | General format

 
%g 與 %e 的不同

```
'e' 
Exponent notation. Prints the number in scientific notation using the letter ‘e’ to indicate the exponent. 
The default precision is 6.
```

```
'g'
General format. For a given precision p >= 1, this rounds the number to p significant digits and then formats the 
result in either fixed-point format or in scientific notation, depending on its magnitude.
```

```python
>>> "%.3e" % 123
'1.230e+02'
>>> "%.3g" % 123
'123'
>>> "%.3e" % 1234
'1.234e+03'
>>> "%.3g" % 1234
'1.23e+03'
```

<br><br>

### 輸入

運用函數 `input()` 來實現輸入數據，輸入的數據皆為 `str` 類型

```python
>>> a = input()
123
>>> type(a)
<class 'str'>
```

<br><br>

### 運算符號
<br>

算術運算符號

| 符號   | 意義 
| :---: | :---:  
| +     | 加
| -     | 剪
| *     | 乘
| /     | 除
| //    | 除後取商
| %     | 除後取餘 
| **    | 次方

```python
>>> a = 5
>>> b = 2
>>> a + b
7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a // b
2
>>> a % b
1
>>> a ** b
25
```

覆值運算符號

| 符號   | 意義 
| :---: | :---:  
| =     | 將覆值符號右邊結果給左邊的變量

```python
>>> a, b = 1, 2
>>> a
1
>>> b
2
```

複合覆值運算符號

| 符號   | 意義 
| :---: | :---:  
| +=     | a += b 等效 a = a + b
| -=     | a -= b 等效 a = a - b
| *=     | ---
| /=     | ---
| //=    | ---
| %=     | ---
| **=    | ---

<br><br>

### 數據類型的轉換
<br>

常用的數據類型轉換函數

| 函數   | 意義 
| :---: | :---:  
| int(x, base)          | 以底為 base 轉換 x 為十進位
| float(x)              | 轉換為浮點數
| complex(real, imag)   | 創建複數
| str(x)                | 轉換為字符串
| eval(string)          | 用來計算字符串中有效的表達式
| tuple(s)              | 轉換為元組
| list(s)               | 轉換為列表
| hex(x)                | 轉換為十六進制字符串

```python
>>> int('11', 16)
17
>>> float(10)
10.0
>>> complex(1,1)
(1+1j)
>>> str(10)
'10'
>>> eval('1 + 1')
2
>>> tuple({1,2})
(1, 2)
>>> list('123')
['1', '2', '3']
>>> hex(11)
'0xb'
```

<br><br>

### 比較運算符號
<br>

Python 中的比較運算符號

| 符號   | 意義 
| :---: | :---:  
| ==     | 等於
| !=     | 不等於 (較常用)
| <>     | 不等於
| >      | 大於
| <      | 小於
| >=     | 大於或等於
| <=     | 小於或等於

Python 中的邏輯運算符號

| 符號   | 意義 
| :---: | :---:  
| and    | True if both the operands are true
| or     | True if either of the operands is true
| not    | True if operand is false

> [更多的相關運算符號](https://www.programiz.com/python-programming/operators) :arrow_left:

<br><br>

## 判斷與循環


