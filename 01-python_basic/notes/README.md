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
    * [if-else-elif](#if-else-elif)
    * [while](#while)
    * [for](#for)
    * [break & continue](#break-&-continue)
* **[資料類型](#資料類型)**
    * [字串](#字串)
    * [列表](#列表) 
    * [元組](#元組)
    * [字典](#字典)
    * [公用方法](#公用方法)
    * [視覺化](#視覺化)
* **[函數](#函數)**
    * [函數介紹](#函數介紹)
    * [定義函數](#定義函數)
    * [變量](#變量)
    * [參數](#參數)
    * [遞迴函數](#遞迴函數)
    * [匿名函數](#匿名函數)
* **[文件操作和應用](#文件操作和應用)**
    * [文件相關操作](#文件相關操作)
    * [文件夾相關操作](#文件夾相關操作)
* **[物件導向程式設計](#物件導向程式設計-(object-oriented-programming))** 
    * [類型與物件](#類型與物件-(class,-object))
    * [方法與屬性](#方法與屬性-(method,-attribute))
    * [繼承、封裝、多型](#繼承、封裝、多型)
    * [設計模式](#設計模式-(design-pattern))


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

> [Hint : 利用 `format()` 取代 `%s`](https://pyformat.info/)

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

> Hint: [更多的相關運算符號](https://www.programiz.com/python-programming/operators)

<br><br>

## 判斷與循環
<br><br>

### if-else-elif
<br>

1. 當需要滿足某些條件 **A** 時，需要使用 `if`
2. 當滿足條件 **A** ，不滿足時需要執行其他事件時，需要使用 `else`
3. 當滿足條件 **A** 執行事件一， 滿足條件 **B** 執行事件二 ...，需要使用 `elif`

```
if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else
```


<br><br>

### while
<br>

```
while test_expression:
    Body of while
else:
    Run when the condition is False
```

[練習 : 印出三角形](../while/print_triangle.py)

```
*
**
***
****
*****
```

[練習 : 印出九九乘法表](../while/print_9x9.py)

```
1*1=1  
1*2=2  2*2=4  
1*3=3  2*3=6  3*3=9  
1*4=4  2*4=8  3*4=12 4*4=16 
1*5=5  2*5=10 3*5=15 4*5=20 5*5=25 
1*6=6  2*6=12 3*6=18 4*6=24 5*6=30 6*6=36 
1*7=7  2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49 
1*8=8  2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64 
1*9=9  2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81  
```

<br><br>

### for
<br>

```
for val in sequence:
	Body of for
else:
    Run if the items in the sequence used in for loop exhausts
```

<br><br>
### break & continue
<br>

#### break
用來結束整個循環

#### continue
用來結束此次循環，並執行下一次的循環

<br><br>

## 資料類型
<br><br>

### 字串
<br>

#### 介紹

可以用一個變量來存儲字串

```python
s = "hello python"
```

<br>

#### 輸出

```python
name = 'felix'
position = "Engineer"
introduction = """ Hello Everyone!
I am a newbie to this company.
Happy to join this team."""

print("name:%s"%name)
print("position:%s"%position)
print("introduction:%s"%introduction)
```

```
name:felix
position:Engineer
introduction: Hello Everyone!
I am a newbie to this company.
Happy to join this team.
```

<br>

#### 輸入

```python
username = input('please input the name:')
print("username is %s" %username)
```

```
please input the name:Felix
username is Felix
```

<br>

#### 索引

用索引取出部份字串

```python
>>> name = 'abcdef'
>>> name[1]
'b'
```

如果索引超過字串長度會產生 `IndexError`

```python
>>> name = 'abcdef'
>>> name[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

如果索引值不為整數會產生 `TypeError`

```python
>>> name = 'abcdef'
>>> name[2.5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers
```

<br>

#### Slice

Slice 是指對操作的對象擷取其中一部份， string 、 list 、 tuple 都支援此用法

> Slice 語法 : \[起始:結束:步長\]

[練習 : 反轉字串](../string/str_manipulation.py)

<br>

#### 常見操作

find

```python
s.find(str, start=0, end=len(mystr))
```

```python
# if found, return the index
>>> s = 'hello python world!'
>>> s.find('python')
6
# if not found, return -1
>>> s.find('python',0 ,5)
-1
```

rfind

與 `find` 相同，但是從右邊開始找

```python
s.rfind(str, start=0, end=len(mystr))
```


index

與 `find` 相同，但在沒找到時返回 `ValueError`

```python
s.index(str, start=0, end=len(mystr))
```

```python
>>> s = 'hello python world!'
>>> s.index('python')
6
>>> s.index('python',0, 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

rindex

與 `index` 相同，但是從右邊開始找

```python
s.rindex(str, start=0, end=len(mystr))
```

count

返回要搜尋字串出現的次數

```python
s.count(str, start=0, end=len(mystr))
```

replace

將 `s1` 替換成 `s2` 如果指定 `count` 則不超過次數

```python
s.replace(s1, s2,  s.count(s1))
```

```python
>>> s = "ha ha"
>>> s.replace("ha", "HA")
'HA HA'
>>> s.replace("ha", "HA", 1)
'HA ha'
```

split

```python
s.split(splitor, maxsplit)    
```

```python
>>> s = "hello world python"
>>> s.split(" ")
['hello', 'world', 'python']
>>> s.split(" ",1)
['hello', 'world python']
```

capitalize

將字串的第一個字變為大寫

```python
s.caplitalize()    
```

title

將字串的每個單字字首變為大寫

```python
s.title()    
```

stratswith

檢查字串是否為 `start_string` 開頭

```python
s.startswith(start_string)    
```

```python
>>> s = "hello world python"
>>> s.startswith("hello")
True
>>> s.startswith("python")
False
```

endswith

檢查字串是否為 `end_string` 結尾

```python
s.endswith(end_string)    
```

lower

轉換字串中所有大寫字母為小寫

```python
s.lower()
```

upper

轉換字串中所有小寫字母為大寫

```python
s.upper()
```

lstrip

刪除字串左邊的空白

```python
s.lstrip()
```

rstrip

刪除字串右邊的空白

```python
s.rstrip()
```

strip

刪除字串兩邊的空白

```python
s.strip()
```

isdigit

如果字串只包含數字返回 `True` 否則返回 `False`

```python
s.isdigit()
```

```python
>>> s = 'abc123'
>>> s.isdigit()
False
>>> s = '123'
>>> s.isdigit()
True
```

join

讓列表每個字串後插入特定字符，構造成新字串

```python
s.join(list)
```

```python
>>> l = ["hello", "world", "python"]
>>> s = ""
>>> s.join(l)
'helloworldpython'
>>> s = " "
>>> s.join(l)
'hello world python'
>>> s = ","
>>> s.join(l)
'hello,world,python'
```

<br><br>

### 列表

<br>

#### 介紹

可以用一個變量來存儲列表

```python
l = ["hello", "world", "python"]
```

#### 輸出

```python
>>> l = ["hello", "world", "python"]
>>> print(l)
['hello', 'world', 'python']
>>> print(l[0])
hello
>>> print(l[1])
world
>>> print(l[2])
python
```

#### 遍歷

for

```python
l = ["hello", "world", "python"]

for i in l:
    print(i)
```


while

```python
l = ["hello", "world", "python"]

length = len(l)

i = 0

while i < length:
    print(l[i])
    i += 1
```

#### 常見操作

可以對列表中存放的數據進行，增、刪、改、查

添加元素

可以通過 `append` `extend` `insert` 來對列表添加元素

```python
>>> a = [1, 2]
>>> b = [3, 4]
>>> a.append(b)
>>> a
[1, 2, [3, 4]]
>>> a.extend(b)
>>> a
[1, 2, [3, 4], 3, 4]
>>> a.insert(2,3)
>>> a
[1, 2, 3, [3, 4], 3, 4]
```

更改元素

可以通過對**索引值**的操作對列表更改元素

```python
>>> a = [1, 2, 3, 4]
>>> a[0] = 0
>>> a
[0, 2, 3, 4]
```

查找元素

可以通過 `in` `not in` `index` `count` 來查找列表元素

```python
l = [1, 2, 3, 4]

if 1 in l:
    print('found')
else:
    print('not found')
```

```python
>>> l = [1, 2, 3, 4, 5, 6]
>>> l.index(1)
0
>>> l.index(1, 1, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 1 is not in list
>>> l.count(1)
1
>>> l.count(7)
0
```

刪除元素

可以通過 `del` `pop` `remove` 將列表中元素刪除

`del` 可以將整個列表刪除，也可將特定索引值刪除

`pop` 將列表最後一個元素刪除，也可將特定索引值刪除，會返回刪除的元素值

```python
>>> l
['a', ''b', 'c', 'd', 'a', 'b', 'c', 'd']
>>> del l[0]
>>> l
['b', 'c', 'd', 'a', 'b', 'c', 'd']
>>> l.remove('c')
>>> l
['b', 'd', 'a', 'b', 'c', 'd']
>>> l.pop()
'd'
>>> l.pop(2)
'a'
>>> l
['b', 'd', 'b', 'c']
```

排序

可以通過 `sort` `reverse` 對列表排序

```python
>>> l = [1, 3, 2, 4]
>>> l
[1, 3, 2, 4]
>>> l.reverse()
>>> l
[4, 2, 3, 1]
>>> l.sort()
>>> l
[1, 2, 3, 4]
>>> l.sort(reverse=True)
>>> l
[4, 3, 2, 1]
```

<br><br>

### 元組
<br>

元組的元素無法被修改

```python
t = (1, 2, 3)
```

元組的內建函數 `count` `index`

```python
>>> t = ('a', 'b', 'c', 'a', 'b')
>>> t.index('a')
0
>>> t.index('a', 1, 5)
3
>>> t.count('b')
2
>>> t.count('d')
0
```

<br><br>

### 字典
<br>

#### 介紹

字典是由鍵值對組成，根據查找鍵來得到相對應的值

```python
d = {key: value}
```

#### 遍歷

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> for key, value in d.items() :
...     print(key, value)
... 
a 1
c 3
b 2
```


#### 常見操作

字典的與列表類似，也可以對字典中存放的數據，增、刪、改、查

添加元素

可以通過對不存在的鍵覆值，新增元素

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> d['d'] = 4
>>> d
{'a': 1, 'c': 3, 'b': 2, 'd': 4}
```

修改元素

可以通過對存在的鍵覆值，修改元素

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> d['c'] = 4
>>> d
{'a': 1, 'c': 4, 'b': 2}
```

查找元素

可以通過 `get` ，查找元素

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> d.get('a')
1
```


刪除元素

可以通過 `del` 刪除整個字典，或刪除特定元素

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> del d['a']
>>> d
{'c': 3, 'b': 2}
```

清空元素

可以通過 `clear` 清空字典

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> d.clear()
>>> d
{}
```

<br>

字典其他常用的操作

len

字典鍵值對的個數

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> len(d)
3
```

keys

字典中所有鍵，返回類型為 `dict_keys` ，可以用 `list` 轉換成列表使用

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> a = d.keys()
>>> type(a)
<class 'dict_keys'>
>>> b = list(d.keys())
>>> b
['a', 'c', 'b']
```

values

字典中所有值，返回類型為 `dict_values` ，可以用 `list` 轉換成列表使用

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> a = d.values()
>>> a
dict_values([1, 3, 2])
>>> b = list(d.values())
>>> b
[1, 3, 2]
```

items

字典中所以鍵值，返回類型為 `dict_items`， 可以用 `list` 轉換成列表使用

```python
>>> d = { 'a' : 1, 'b':2, 'c':3 }
>>> d.items()
dict_items([('a', 1), ('c', 3), ('b', 2)])
>>> list(d.items())
[('a', 1), ('c', 3), ('b', 2)]
```

<br><br>

### 公用方法

<br>


<br><br>

### 視覺化

<br>

<br><br>

## 函數

<br><br>

### 函數介紹
<br>

在開發時，某塊程式碼會重複使用到，為了提高效率和程式碼的重用性，所以把其功能獨立出來為一函數

<br><br>

### 定義函數
<br>

四種函數的類型

* 無參數，無返回值
* 無參數，有返回值
* 有參數，無返回值
* 有參數，有返回值

```
def add2num(a, b):
    return a + b

print(add2num(1, 2))
```

[函數的運作](http://www.pythontutor.com/visualize.html#code=def%20add2num%28a,%20b%29%3A%0A%20%20%20%20return%20a%2Bb%0A%0Aprint%28add2num%2811,%2022%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


<br><br>

### 變量
<br>

#### 全局變量

作用域為整個程式執行範圍

```python
x = "global"

def test():
    print("x inside :", x)

test()
print("x outside:", x)
```

```
x inside : global
x outside: global
```

#### 局部變量

作用域為函數執行範圍

```python
def test():
    y = "local"

test()
print(y)
```

```
NameError: name 'y' is not defined
```


#### 全局變量與局部變量

在函數內如要對全局變量做修改需要宣告 `global`

> Hint: 當列表和字典作為全局變量時，在函數內是不需要宣告 `global` 即可對其修改

```python
x = "global"

def test():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
    
test()
```

```
global global 
local
```

如果沒有宣告 `global` ，在函數內又定義相同名稱變量，則為局部函數視之

```python
x = 5

def test():
    x = 10
    print("local x:", x)

test()
print("global x:", x)
```

```
local x: 10
global x: 5
```

#### 非局部變量

在巢狀函數中，如果內部函數要對外部函數變量進行修改，則需宣告 `nonlocal`

```python
def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()
```

<br><br>

### 參數

<br>

#### 介紹

> "We will generally use parameter for a variable named in the parenthesized list in a function definition, and argument for the value used in a call of the function. The terms formal argument and actual argument are sometimes used for the same distinction."
>
>  ——《The C Programming Language》Section 1.7 K&R

`parameter` 形式參數，在函數定義時，所定義的參數通常以此稱之

`argument` 實際參數，在呼叫函數時，傳入的參數通常以此稱之

在 Python 中，參數皆稱為 `argument` 沒有區分

#### 位置參數 (positional arguments)

一般需要覆值的參數

#### 預設參數 (default arguments)

呼叫函數時，如果預設參數沒有被覆值，則為預設值。

```python
def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce",msg = "How do you do?")
```

定義函數和呼叫函數時，帶有預設值的參數皆要位於無預設值參數的後方

```python
def greet(msg = "Good morning!", name):
```

```
SyntaxError: non-default argument follows default argument
```

#### 不定長度參數 (arbitrary arguments)



#### 關鍵字參數 (keyword arguments)

#### 命名關鍵字參數


<br><br>

### 遞迴函數
<br>

如果函數在內部呼叫自己本身的話，這個函數稱為遞迴函數

* 優點
    * 遞迴函數讓程式碼看起來簡化且乾淨
    * 可以將一個複雜的問題，拆分成數個子問題來看待 `divide and conquer`
* 缺點
    * 背後的邏輯有時較難弄懂
    * 會佔用較多的記憶體和時間
    * 偵錯比較困難

[練習 : 遞迴函數計算階層](../recursion/recursive.py) 

[遞迴函數的運作](http://www.pythontutor.com/visualize.html#code=def%20calc_factorial%28num%29%3A%0A%20%20%20%20%22%22%22This%20is%20a%20recursive%20function%0A%20%20%20%20%20%20%20%20to%20find%20the%20factorial%20of%20an%20integer%22%22%22%0A%20%20%20%20if%20num%20%3E%201%3A%0A%20%20%20%20%20%20%20%20return%20num%20*%20calc_factorial%28num-1%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20num%0A%0Anum%20%3D%205%0A%0Aprint%28%22The%20factorial%20of%22,%20num,%20%22is%22,%20calc_factorial%28num%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

<br><br>

### 匿名函數 (lambda function)
<br>

```
lambda arguments: expression
```

匿名函數省略了用 `def` 聲明函數的標準步驟

```python
square = lambda x: x ** 2
```

```python
def square(x):
    return x ** 2
```

[練習 : 依照姓名和年紀排序](../lambda/lamba_sort.py)

#### 進階應用

[Map, Filter and Reduce](http://book.pythontips.com/en/latest/map_filter.html)


<br><br>

## 文件操作和應用

<br><br>

### 文件相關操作
<br>

#### 開啟與關閉

```
f = open("test.txt",mode = 'r',encoding = 'utf-8')
f.close()
```

使用 `with` 開啟文件可以不需要再呼叫 `close()` 關閉文件

```
with open("test.txt",encoding = 'utf-8') as f:
```


| 模式   | 說明 
| :---: | :---:  
| r     | 用讀方式打開文件，文件的指針會在文件的開頭
| w     | 用寫方式打開文件，如果文件存在將其覆蓋，如果文件不存在創造新文件
| a     | 用追加方式打開文件，文果文件存在指針將會在文件結尾，如果文件不存在創造新聞鍵
| b     | 用二進制打開文件
| +     | 允許讀寫操作

<br>

#### 讀取與寫入

#### 相關操作

[文件詳細操作說明](https://www.programiz.com/python-programming/file-operation#methods)

[練習 : 讀取與寫入操作](../file_operation/write_read_file.py)

[練習 : 製作文件備份](../file_operation/copy_file.py)

#### 定位讀寫

獲取當前文件的位置 `tell()`

```python
>>> f = open("read_write_file.bak", "r" , encoding = "utf-8")
>>> f.read(3)
'tes'
>>> f.tell()
3
>>> f.read(3)
't !'
>>> f.tell()
6
>>> f.close()
```

定位到文件的某個位置 `seek()`

* `seek(offset, from)`
    * offset : 偏移量
    * from : 從哪裡開始
        * 0 : 文件開頭
        * 1 : 當前位置
        * 2 : 文件結尾

將指針設定為，從文件開頭，偏移 5 個字節

```python
>>> f = open("read_write_file.bak", "r" , encoding = "utf-8")
>>> f.read(15)
'test !!!! \ntest'
>>> f.tell()
15
>>> f.seek(5,0)
5
>>> f.tell()
5
>>> f.close()
```

將指針設定為，文件尾端


> In text files (those opened without a `b` in the mode string),
> only seeks relative to the beginning of the file are allowed
> (the exception being seeking to the very file end with `seek(0, 2)`).


```python
>>> f = open("read_write_file.bak", "r" , encoding = "utf-8")
>>> f.tell()
0
>>> f.seek(-3,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: can't do nonzero end-relative seeks
>>> f.seek(0,2)
44
>>> f.close()
```

<br><br>

### 文件夾相關操作

<br>

利用 `os` 模組來達到文件與文件夾的相關操作

#### 當前資料夾

```python
>>> os.getcwd()
'/home/felixlin/road_to_python/01-python_basic/file_operation'
>>> os.getcwdb()
b'/home/felixlin/road_to_python/01-python_basic/file_operation'
```

#### 更換資料夾

```python
>>> os.chdir('../')
>>> os.getcwd()
'/home/felixlin/road_to_python/01-python_basic'
```

#### 獲取資料夾列表

```python
>>> os.listdir("file_operation")
['write_read_file.py', 'read_write_file.txt', 'copy_file.py', 'read_write_file.bak']
```

#### 創建新資料夾

```python
>>> os.mkdir('test')
>>> os.listdir()
['test']
```

#### 重新命名

```python
>>> os.listdir()
['test']
>>> os.rename('test','new_one')
>>> os.listdir()
['new_one']
```

#### 刪除

```python
>>> os.listdir()
['new_one', 'old.txt']
>>> os.remove('old.txt')
>>> os.listdir()
['new_one']
```

#### 批次修改文件名

<br><br>

## 物件導向程式設計 (Object-oriented programming)

<br><br>

### 類型與物件 (class, object)

<br>

#### 類型

定義了物件能實現的抽象屬性和方法

定義類型

```python
class MyFirstClass:
    '''This is a docstring. I have created my first class'''
    pass
```

#### 物件

又稱為類型的實例 (instance) ，透過將類型實例化 (instantiation) 得到實體物件

創建實例

```python
obj = MyFirstClass()
```

[練習 : 定義類型，創建實例，添加方法與屬性](../OOP/OOP.py)

<br><br>

### 方法與屬性 (method, attribute)

<br>

* 方法是用來描述物件的行為
* 屬性是用來描述物件的特徵

```python
class Parrot:

    # class attribute
    species = "bird"

    # magic method
    def __init__(self, name, age):
    # instance attribute
        self.name = name
        self.age = age
    
    def __str__(self):
        return "species: {}, name: {}, age: {}".format(self.species, self.name, self.age)
    
 
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# call the __str__ method
print(blu)
print(woo)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

# call instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
```

#### 魔法方法 (magic methods)

[魔法方法詳細介紹](https://rszalski.github.io/magicmethods/)

`__init__()`

當創建實例時， `__init__()` 方法隨即會被呼叫，用來初始化

`__init__(self, name, age)` 在定義類型時，定義需要的傳入的參數


`__str__()`

當要輸出物件時，即會輸出 `__str__()` 方法定義的返回值

`__del__()`

當刪除實例時， `__del__()` 方法隨即會被呼叫

當有其他變量也指到同一物件時，會等到所有的引用接被刪除才會呼叫 `__del__`

[練習 : `__del__` 方法](../OOP/OOP__del__.py)


`__new__`

實例化時最先呼叫的類型方法，作用為返回類型的新實例

```python
class MyClass(object):
    def __init__(self):
        print("this is init method")

    def __new__(cls):
        print("this is new method")
        return object.__new__(cls)
```

實際應用，將 inch 轉換為 meter

```python
>>> class InchToMeter(float):
    ...     "Convert from inch to meter"
    ...     def __new__(cls, arg=0.0):
    ...         return float.__new__(cls, arg*0.0254)
    ...
    >>> print (InchToMeter(12))
    0.30479999999999996
```



<br>

#### 實例屬性

`self`

`self` 為實例屬性，在實例化時，需要對 `__init__(self)` 調用實例屬性來初始化

同一類型所創建的各個實例，實例屬性為獨立


<br>

#### 類型屬性

`species` 為類型屬性，同一類型所創建的各個實例，會共享此一類型屬性 

<br>

#### 實例方法

`def sing(self, song)` 在定義實例方法時，將需要傳入的參數定義在 `self` 之後


<br>

[練習 : 存放家具]()

<br>

#### 私有屬性

對實例屬性修改的方式有兩種

1. object.attr = data  `直接修改屬性值`
2. object.method(data) `透過呼叫實例方法修改屬性值`

私有屬性，不允許實例化的物件訪問，但允許實例方法訪問

```python
>>> class Myclass:
...     def __init__(self):
...             self.__age = 18
... 
>>> Myclass.__age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Myclass' has no attribute '__age'
```

私有類屬性，實際上被重寫為 `_classname__attribute`，所以在屬性命名時要注意，不然會混淆

```python
>>> class Myclass:
...     __name = "Felix"
... 
>>> dir(Myclass)
['_Myclass__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> Myclass._Myclass__name
'Felix'
```

<br>

#### 私有方法

私有方法，不允許實例訪問，但實際上被重寫為 `_classname__method`，所以在方法命名時也需要注意，不然會混淆

[練習 : 私有方法](../OOP/OOP_private_method.py)

<br>

#### 類型方法

需要用裝飾器 `@classmethod` 來標示為類方法，可以用來訪問和修改類屬性

[練習 : 類方法與靜態方法](../OOP/OOP_instance_class_static_method.py)

<br>

#### 靜態方法

需要用裝飾器 `@staticmethod` 來標示為靜態方法，不需要多定義參數

<br>

> 總結
>
> 類方法的第一個參數是類物件 `cls` ，通過 `cls` 引用的必定是類物件的屬性和方法
> 
> 實例方法的第一個參數是實例物件 `self` ，通過 `self` 引用的可能是類屬性，也有可能是實例屬性，在存在同名稱的情況下，實例屬性的優先權較高
>
> 靜態方法不需要任何參數，在靜態方法中引用類屬性，必須通過類物件來引用，無法引用實例屬性



<br><br>

### 繼承、封裝、多型

<br>

#### 繼承 (inheritance)

父類的屬性及方法皆會被繼承

```python
class BaseClass:
  # Body of base class
class DerivedClass(BaseClass):
  # Body of derived class
```

單繼承

私有的属性、方法，不会被子類继承，也不能被子類直接被訪問

[練習 : 單繼承，並重寫父類方法](../OOP/OOP_inherit.py)

重寫

在子類中，定義和父類相同名字的方法，子類的方法會將父類方法覆蓋

子類可以通過 `super()` 來呼叫父類的實例方法


多繼承

子類繼承多個父類類型，如遇到同名字的實例方法，可以用 `__mro__` 來查看先後順序

這個搜索方法稱為 [C3 Algorithm](http://search.cpan.org/~haarg/Algorithm-C3-0.10/lib/Algorithm/C3.pm)

[練習 : 多繼承，並查看實例方法搜索的先後順序](../OOP/OOP_muti_inherit.py)

<br>

#### 封裝 (encapsulation)

封裝，又稱資料封裝，運用私有屬性防止物件中的資料被直接的修改


<br>

#### 多型 (polymorphism)

鴨子類型 `duck typing`

在鴨子型別中，關注點在於物件的行為，能作什麼；而不是關注物件所屬的類型。

在多型的應用中，運用相同的界面，傳入不同的子類將會產生不同的行為，無須明確知道子類實際上是什麼。

[練習 : 多型](../OOP/OOP_polymorphism.py)


<br><br>

### 設計模式 (design pattern)

<br>

> 設計模式的目的是讓程式碼易於維護和擴展


#### 簡單工廠模式 (simple factory pattern)

通過一個工廠來決定創建哪些實體產品

組成要素

* 工廠
    * 可以用類型或函數實現，負責產品實例的創建
* 產品的模板
    * 通常用類型實現，提供子類產品通用的屬性和方法
* 產品
    * 通常用類型實現，繼承父類模板衍生出各種具體的產品

> 通過經典的案例來演示簡單工廠模式
>
> [練習 : 計算機](../OOP/simple_factory_calc.py)
> 
> [練習 : 車商](../OOP/car_store.py)

<br>

#### 工廠方法模式 (factory method pattern)


<br>

#### 單例模式 (singleton pattern)

確保某個類型只有一個實例

當每個實例都會占用資源，並且實例初始化會影響性能，此時就可以考虑使用單例模式，它给我们带来的好处是只有一个实例占用资源，并且只需初始化一次；

[練習 : 單例模式](../OOP/singleton.py)

<br><br>

## 異常處理

<br><br>

### 異常 (exception)

<br>

當 python 解釋器偵測到錯誤時，導致解釋器中斷無法繼續運行，而出現的錯誤提示

[詳細的異常](https://www.programiz.com/python-programming/exceptions)

```python
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> open("test.txt")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
```

<br><br>

### 異常處理

<br>

####單一異常處理

此程序看不到任何錯誤，因為用 `except` 處理異常 `IOError`

```python
try:
    print('-----test--1---')
    open('test.txt','r')
    print('-----test--2---')
except IOError:
    pass
```

<br>

####多個異常處理

將多個異常名字用元組方式處理

```python
try:
    # FileNotFoundError
    open("_.txt")
    
    # NameError
    print(num)

# use tuple to combine exception
except (NameError, FileNotFoundError) as e:
    print("Deal with Exception")
    print(e)
```

<br>

####所有異常處理

```python
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except Exception:
   # handle all other exceptions
   pass

else:
    # no exception occurs
    pass
    
finally:
    # no matter if the exception occurs, do this
    pass
```

<br>

#### 自定義異常處理

