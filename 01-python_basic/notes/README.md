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

### 介紹
<br>

在開發時，某塊程式碼會重複使用到，為了提高效率和程式碼的重用性，所以把其功能獨立出來為一函數

<br><br>

###定義函數
<br>

```
def add2num(a, b):
    return a + b

print(add2num(1, 2))
```

[函數的運作](http://www.pythontutor.com/visualize.html#code=def%20add2num%28a,%20b%29%3A%0A%20%20%20%20return%20a%2Bb%0A%0Aprint%28add2num%2811,%2022%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)



