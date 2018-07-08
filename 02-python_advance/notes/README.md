# Python Advance Notes
<br>

## 目錄
* **[進階物件導向程式設計](#進階物件導向程式設計)**
    * [元類型](#元類型-metaclass)
    * [動態語言](#動態語言)
    * [迭代器](#迭代器-iterator)
    * [生成器](#生成器-generator)
    * [閉包](#閉包-closure)
    * [裝飾器](#裝飾器-decorator)
* **[Python 進階知識](#Python-進階知識)**
    * [模組導入](#模組導入)
    * [作用域](#作用域)
    * [淺複製、深複製](#淺複製、深複製)
    * 
* **[正規表達式](#正規表達式-regular-expression)**
    *


<br><br>
## 進階物件導向程式設計

<br><br>
### 元類型 (metaclass)
<br>

原文在 [stackvoerflow](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python) 上的解釋

<br>

![metaclass_img](images/metaclass.png)

#### 類型也是物件

類型是用來描述如何產生物件的程式碼

```python
>>> class ObjectCreator(object):
…       pass
…
>>> my_object = ObjectCreator()
>>> print(my_object)
<__main__.ObjectCreator object at 0x7fcbe94f4518>
```

而在 python 中，類型就是物件本身，在使用關鍵字 `class` 時，python 解釋器在執行中會創建一個物件，這個物件擁有創造新的物件的能力。

所以可以對類型的這個物件，做以下操作 :

1. 將它覆值給一個變量
2. 複製它
3. 為它增加屬性
4. 將它做為函數參數傳遞

```python
# you can print a class because it's an object
>>> print(ObjectCreator)
<class '__main__.ObjectCreator'>
>>> def echo(o):
...     print(o)
... 
# you can pass a class as a parameter
>>> echo(ObjectCreator)
<class '__main__.ObjectCreator'>
>>> print(hasattr(ObjectCreator, 'new_attribute'))
False
# you can add attributes to a class
>>> ObjectCreator.new_attribute = 'foo'
>>> print(hasattr(ObjectCreator, 'new_attribute'))
True
>>> print(ObjectCreator.new_attribute)
foo
# you can assign a class to a variable
>>> ObjectCreatorMirror = ObjectCreator
>>> print(ObjectCreator())
<__main__.ObjectCreator object at 0x7fcbe8dfac88>
```

<br>

#### 動態創造類型

類型也是物件，就像其他任何物件一般，可以動態創造它

首先，可以利用 `class` 在函數中創建一個類型

```python
>>> def choose_class(name):
...     if name == 'foo':
...         class Foo(object):
...             pass
...         return Foo # return the class, not an instance
...     else:
...         class Bar(object):
...             pass
...         return Bar
...
>>> MyClass = choose_class('foo')
>>> print(MyClass) # the function returns a class, not an instance
<class '__main__.Foo'>
>>> print(MyClass()) # you can create an object from this class
<__main__.Foo object at 0x89c6d4c>
```

因為仍然需要創建類型本身，顯得不夠動態

可以思考的是類型也是物件，應當是可以通過其它東西來生成

而當使用 `class` 時， python 自動生成類型這個物件，而也要有方法可以手動生成這個物件才是

回想函數 `type` ，這個古老且強大的函數可以了解一個物件的類型是什麼

```python
>>> print(type(1))
<class 'int'>
>>> print(type('1'))
<class 'str'>
>>> print(type(ObjectCreator))
<class 'type'>
>>> print(type(ObjectCreator()))
<class '__main__.ObjectCreator'>
```

其實， `type` 還有一種完全不同的功能，就是動態的創造類型

`type` 可以接收一個類型的描述做為參數，返回一個類型

> 要知道，一個函數根據不同傳入的參數有不同的用法，是一件很蠢的事情，但在 python 中這樣的用義是為了向後的兼容性

```
type(name of the class,
     tuple of the parent class (for inheritance, can be empty),
     dictionary containing attributes names and values
    )
```

用 `class` 生成的類型對應到用 `type` 生成的類型

```python
>>> class MyShinyClass(object):
...       pass
```

```python
>>> MyShinyClass = type('MyShinyClass', (), {}) # returns a class object
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'>
>>> print(MyShinyClass()) # create an instance with the class
<__main__.MyShinyClass object at 0x8997cec>
```

如果需要在類型裡加入類型屬性，可以將用字典形式當作參數傳入 `type`

```python
>>> class Foo(object):
...       bar = True
```

```python
>>> Foo = type('Foo', (), {'bar':True})
>>> print(Foo)
<class '__main__.Foo'>
>>> print(Foo.bar)
True
>>> f = Foo()
>>> print(f)
<__main__.Foo object at 0x8a9b84c>
>>> print(f.bar)
True
```

當然也可以繼承，用元組的形式當作參數傳入 `type`

```python
>>>   class FooChild(Foo):
...         pass
```

```python
>>> FooChild = type('FooChild', (Foo,), {})
>>> print(FooChild)
<class '__main__.FooChild'>
>>> print(FooChild.bar) # bar is inherited from Foo
True
```

最終，如果想要在類型裡增加方法的話，只需要定義函數將它作為屬性覆值即可

增加實例方法，靜態方法，類型方法

```python
>>> def echo_bar(self):
...       print(self.bar)
...
>>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
>>> hasattr(Foo, 'echo_bar')
False
>>> hasattr(FooChild, 'echo_bar')
True
>>> my_foo = FooChild()
>>> my_foo.echo_bar()
True
```

並且就像正常的創建類型增加新的方法一樣，在動態創建類型後也可以相同使用

```python
>>> def echo_bar_more(self):
...       print('yet another method')
...
>>> FooChild.echo_bar_more = echo_bar_more
>>> hasattr(FooChild, 'echo_bar_more')
True
```


#### 最終，到底什麼是元類型

元類型是用來創建類型(物件)，元類型被視為類型的類型

```python
MyClass = MetaClass()
my_object = MyClass()
```

```python
MyClass = type('MyClass', (), {})
```

`type` 就是 python 背後用來創建所有類型的元類型，可能會猜想為什麼 `type` 為什麼不是 `Type`，猜測可能是為了和 `str` 和 `int` 保持一致性`str` 和 `int` 分別是創建字串和整數物件的類型，可以通過檢查 `__class__` 來確認這一點

python 中所有的東西，都是物件，這包括整數、字串、函數、類型，而它們都是從 `type` 類型創建出來

```python
>>> age = 35
>>> age.__class__
<type 'int'>
>>> name = 'bob'
>>> name.__class__
<type 'str'>
>>> def foo(): pass
>>> foo.__class__
<type 'function'>
>>> class Bar(object): pass
>>> b = Bar()
>>> b.__class__
<class '__main__.Bar'>
```

```python
>>> age.__class__.__class__
<type 'type'>
>>> name.__class__.__class__
<type 'type'>
>>> foo.__class__.__class__
<type 'type'>
>>> b.__class__.__class__
<type 'type'>
```

可以看到對於任何一個物件取 `__class__` 的 `__class__` 皆為 `type`

`type` 是 python 內建的元類型，當然也可以自己定義元類型

<br>

#### `__metaclass__` 屬性

可以在定義一個類型時為其添加 `__metaclass__` 屬性

```python
class Foo(object):
    __metaclass__ = something...
    [...]
```

這麼做的話 python 會用元類型來創建類型 `Foo`，但這裡有些地方需要注意，首先雖然寫了 `class Foo(object)`，但是類型 `Foo` 並未在記憶體中被創建。 python 會在類型的定義中尋找 `__metaclass__` 屬性，如果找到了就會用它來創建類型 `Foo`，如果沒找到，就會用內建函數 `type` 來創建這個類型

所以當定義以下程式碼

```python
class Foo(Bar):
    pass
```

python 會做如下的操作

1. 判斷 `Foo` 中有沒有 `__metaclass__` 這個屬性，如果有， python 會通過其在記憶體中創建一個類型物件
2. 如果 python 沒有找到 `__metaclass__` ，它會繼續在模組中尋找 `__metaclass__`  屬性，並嘗試做和前述相同的操作 ( python3 已經無法在模組中定義元類型)
3. 如果 python 都找不到 `__metaclass__` ，它就會使用父類型 `Bar` 所擁有的元類型，也就是 `type` 

要小心的一點是， `__metaclass__` 屬性是無法被繼承的

現在的問題是，可以在 `__metaclass__` 中放些什麼，而答案是可以創建類型的東西。

而可以創建類型的都西，即是元類型 `type` 和它的子類型

<br>

#### 自定義元類型

元類型的主要目的是為了當創建類型時，可以自動的改變它。通常我們會為 API 做這件事情，希望能創建符合當前環境的類型

假想一個很蠢的例子，決定在模組裡所有類型的屬性都應該是大寫形式，其中一種實現的方式就是在模組級別設定 `__metaclass__` 。通過這種方式，模組中的所有類型會經由元類型來創建，只需要告訴元類型把所有的屬性都改成大寫形式即可

幸運地， `__metaclass__` 可以在任何地方被呼叫，它可以不必是類型的形式

```python
# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
      Return a class object, with the list of its attribute turned
      into uppercase.
    """

    # pick up any attribute that doesn't start with '__' and uppercase it
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    # let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)

# __metaclass__ = upper_attr # this won't work in python3

class Foo(object, metaclass=upper_attr): # 
    # but we can define __metaclass__ here instead to affect only this class
    # and this will work with "object" children
    bar = 'bip'

print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True

f = Foo()
print(f.BAR)
# Out: 'bip'
```

用真正的類型當做元類型

```python
# remember that `type` is actually a class like `str` and `int`
# so you can inherit from it
class UpperAttrMetaclass(type):
    # __new__ is the method called before __init__
    # it's the method that creates the object and returns it
    # while __init__ just initializes the object passed as parameter
    # you rarely use __new__, except when you want to control how the object
    # is created.
    # here the created object is the class, and we want to customize it
    # so we override __new__
    # you can do some stuff in __init__ too if you wish
    # some advanced use involves overriding __call__ as well, but we won't
    # see this
    def __new__(cls, future_class_name,
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # method 1 : but this is not really OOP, We call type directly and we don't override or call the parent __new__.
        # return type(future_class_name, future_class_parents, uppercase_attr)
        
        # method 2 : reuse the type.__new__ method. this is basic OOP, nothing magic in there
        # return type.__new__(cls, future_class_name, future_class_parents, uppercase_attr)
        
        # method 3 : make it even clearner by user super, which will ease inheritance
        return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents, uppercase_attr)
```

關於元類型已經沒有別的可以說了。使用到元類型的程式碼較複雜，這背後的原因並不是因為元類型本身，而是因為你通常會使用元類型去做一些晦澀的事情

確實，元類型特別有用在做一些黑暗魔法的事情，也應此會產生出較複雜的東西。

但就元類型本身而言，其實很簡單

1. 攔截類型的創建
2. 修改類型
3. 返回修改後的類型

<br>

#### 為什麼要用元類型而不是函數



<br>

#### 究竟為什麼要使用元類型

一般來說，根本就用不到它

> 元類型就像是深度的魔法， 99% 的使用者根本不必為這擔心。如果想要弄清楚究竟是否需要用到元類型，那就代表你不需要它。那些實際用到元類型的人，都非常清楚地知道他們需要做什麼，而根本不需要解釋為什麼
>
>  —— Python界的领袖 Tim Peters

元類型的主要用途是創建 API ，一個典型的例子是 Django ORM

它允許這樣的定義

```python
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
```

但是如果你這樣做

```python
guy = Person(name='bob', age='35')
print(guy.age)
```

這並不會返回 `IntegerField` 物件，而是會返回 `int` ，甚至可以直接從資料庫中取出數據

因為 `models.Model` 定義了 `__metaclass__` ，並且使用了一些魔法能夠將 `Person` 轉換成對資料庫的 `complex hook`。 Django 框架將這些看起來很複雜的東西簡單化，藉由著曝光一個簡單的 API 和元類型的使用，並從這個 API 重建程式碼，完成背後真正的工作

<br>

#### 結語

首先，知道了類型其實是能夠創建出類型實例的物件。事實上，類型本身也是元類型的實例

```python
>>>class Foo(object): pass
>>> id(Foo)
142630324
```

python 中的一切都是物件，類型的實例，元類型的實例。除了 `type` 實際上是自己的元類型，這在純 python 上是無法被重現的

元類型是很複雜的，對於非常簡單的類型，可能不希望通過使用元類型來修改，而可以通過其他兩種技術來實現

1. [Monkey patching](https://en.wikipedia.org/wiki/Monkey_patch)
2. class decorators

當需要動態修改類型時， 99% 的時間最好運用這兩種技術，但其實在 99% 的時間裡，根本就不需要動態更改類型

<br><br>

### 動態語言

<br>

#### 動態語言的定義

> 動態語言是在**運行時可以改變其結構**的語言，例如新的函式、物件、甚至代碼可以被引進，已有的函式可以被刪除或是其他結構上的變化

<br>

#### 在運行的過程中給實例添加屬性

動態添加原先沒有定義的屬性給實例

```python
>>> class Person(object):
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age


>>> P = Person("Felix", "24")
>>> P.gender = "male"
>>> P.gender
'male'
```
<br>

#### 在運行的過程中給實例和類型添加方法

* 給實例添加方法需要引入 `types` 模組
    * 直接覆值，但每次呼叫時需要傳入實例當參數
    * 引入 `types` 模組中的 `MethodType` 方法綁定
* 給類型添加方法
    * 直接覆值即可

[練習 : 動態添加方法](../OOP_advance/add_method_to_class_instance.py)

<br>

#### 在運行的過程中刪除屬性與方法

1. `del instance.attribute`
2. `delattr(instance, "attribute_name")`


#### 限制實例能添加的實例屬性

[練習 : 利用 `__slot__` 限制實例屬性](../OOP_advance/_slots_.py)


<br><br>

### 迭代器 (iterator)
<br>

#### 迭代器介紹

迭代是訪問集合元素的一種方式，而迭代器是可以記住遍歷位址的物件，迭代器從集合的第一個元素開始訪問，直到所有元素被訪問完結束

<br>

#### 可迭代物件

以直接可以作用於 `for` 循環的數據類型，統稱為可迭代物件 `iterable`

* 集合數據類型，如 `list` `tuple` `dict` `set` `str`
* 生成器，包含生成器和帶有 `yield` 的生成函數

<br>

#### 判斷是否可迭代 

可以使用 `isinstance(object, Iterable)` 判斷物件是否可迭代

```python
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance(1, Iterable)
False
>>> isinstance((x for x in range(10)), Iterable)
True
```

#### 迭代器

可以利用 `iter()` 將可迭代對象變為迭代器，利用 `next()` 來迭代物件裡的每個元素，當遇到結束時， 異常 `StopIteration` 發生


```python
>>> my_list = [1, 2, 3, 4, 5]
# get an iterator using iter()
>>> my_iter = iter(my_list)
# iterate through it using next()
>>> next(my_iter)
1
>>> next(my_iter)
2
# next(object) is same as object.__next__()
>>> my_iter.__next__()
3
>>> my_iter.__next__()
4
>>> my_iter.__next__()
5
# raise error, when no items left
>>> my_iter.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

而其實 `for` 循環，也是靠著將可迭代的物件轉變成迭代器，進行遍歷

```python
for element in iterable:
    # do something with element
```

```python
# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
```

<br>

#### 自定義迭代器

[練習 : 自定義迭代器](../iterator/self_define_iterator.py)


<br><br>

### 生成器 (generator)

<br>

#### 生成器介紹

受到記憶體限制，創建的物件容量一定是有限的，如果只僅僅需要使用到幾個元素而創造一個大容量的物件，絕大多數的元素佔用的空間都會被浪費。所以如果能按照某種方法推演，在循環的過程中不斷的推演出後續的元素，這樣就可以節省大量的空間。在 python 中，稱其為生成器 `generator`

<br>

#### 用生成器運算式創造生成器

創建生成器可以使用使用生成器運算式 (generator expression)

生成器運算式，和列表運算式的差別只在於 `[]` 和 `()` 的不同

```python
>>> mylist = [1, 2, 3, 4, 5]
>>> L = [x**2 for x in mylist]
>>> L
[1, 4, 9, 16, 25]
>>> G = (x**2 for x in mylist)
>>> G
<generator object <genexpr> at 0x7f2c5d6fe5c8>
```

可以通過呼叫 `next()` 計算生成器的下一個值並返回，當遇到結束時，會產生異常 `StopIteration`，可以用 `for` 循環避免這個問題

```python
>>> next(G)
1
>>> next(G)
4
>>> next(G)
9
>>> next(G)
16
>>> next(G)
25
>>> next(G)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

```python
>>> G = (x**2 for x in mylist)
>>> for x in G:
...     print(x)
... 
1
4
9
16
25
```

<br>

#### 用 `yeild` 創造生成器

[以著名的 `Fibonacci` 數列為例](https://en.wikipedia.org/wiki/Fibonacci_number)

在循環中不斷的呼叫 `yield` ，就會不斷中斷並返回函數內生成器當前的值

```
>>> def fib(times):
...     n = 0
...     a, b = 0, 1
...     while n < times:
...             yield b
...             a, b = b, a+b
...             n += 1
...     return 'done'
... 
>>> F = fib(7)
>>> for x in F:
...     print(x)
... 
1
1
2
3
5
8
13
```

如果需要拿到函數的返回值，需要捕獲異常 `StopIteration`

```python
>>> G = fib(7)
>>> 
>>> while True:
...     try:
...             x = next(G)
...             print(x)
...     except StopIteration as e:
...             print(e)
...             break
... 
1
1
2
3
5
8
13
done
```

<br>

#### 用 `send` 對生成器覆值

了解了 `next()` 對生成器的運作之後之後，另一個重要的函數 `send(msg)` 跟 `next()` 的區別在於 ， `send(msg)` 可以傳遞值給 `yeild` 而 `next()` 無法，只能傳 `None`

```python
>>> def gen():
...     i = 0
...     while i < 5:
...             temp = yield i
...             print(temp)
...             i += 1
... 
>>> 
>>> g = gen()
>>> next(g)
0
>>> next(g)
None
1
>>> next(g)
None
2
>>> next(g)
None
3
>>> next(g)
None
4
>>> next(g)
None
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

```python
>>> g = gen()
>>> g.__next__()
0
>>> g.send('python')
python
1
>>> g.__next__()
None
2
>>> g.send('python2')
python2
3
>>> g.__next__()
None
4
```

<br><br>

### 閉包 (closure)

<br>

#### 定義閉包函數

在函數內部再定義函數，如果內部函數引用到了外部函數的變量，則可產生閉包。閉包用來在函數與變量之間創建關聯性。

[練習 : 閉包](../closure/closure.py)

<br>

#### 閉包的應用

閉包的存在使用了外部函數的變量，同一個函數傳入不同的變量值，就實現了不同的功能。

[練習 : 閉包二維直線方程式](../closure/closure_application.py)

<br><br>

### 裝飾器 (decorator)

<br>

#### 裝飾器介紹

裝飾器可以在程式執行階段，進行動態的修改，這種行為也稱做 `metaprogramming` 

python 裝飾器用 `＠` 符號對函數進行修飾， `＠func` 是 python 的一種語法糖，其目的是為了能優雅的簡化程式碼。

裝飾器的另一優點是可以在無須修改原函數的情況下，對其加上額外的應用功能

* 引入日誌
* 函數執行時間統計
* 執行函數前預備處理
* 執行函數後清理
* 權限檢驗
* 快取

<br>

#### 裝飾器的應用

[練習 : 無參數的被裝飾函數](../decorator/decorator.py)

[練習 : 有參數的被裝飾函數](../decorator/parameter_decorator.py)

[練習 : 有返回值的被裝飾函數](../decorator/has_return_value_decorator.py)

[練習 : 裝飾器帶有參數的被裝飾函數](../decorator/parameter_in_decorator.py)


<br><br>

## Python 進階知識

<br><br>

### 模組導入

<br>



### 作用域

<br>

### 淺複製、深複製


<br><br>

## 正規表達式 (regular expression)

<br><br>

### 概述

<br>

正規表達式使用單字串來匹配某個語法規則的字串，在很多文字編輯器裡，正則運算式通常被用來檢索、替換那些符合某個模式的文字。

<br><br>

### `re` 模組的使用
<br>

```python
# 导入 re 模块
import re

# 使用 match 方法进行匹配操作
result = re.match(正则表达式, 要匹配的字符串)

# 如果上一步匹配到数据的话，可以使用 group 方法来提取数据
result.group()
```

``` python
>>> import re
>>> result = re.match("itcast", "itcast.cn")
>>> result.group()
```

<br><br>

### 字元的匹配

<br>

| 符號   | 功能   |
| :---: | :---   |
|   .   | 匹配任意字元 ( 除了 \n )
|   []  | 匹配 [] 中列舉的字元
|   \d  | 匹配數字 0 - 9
|   \D  | 匹配非數字
|   \s  | 匹配空白， space or tab
|   \S  | 匹配非空白
|   \w  | 匹配文字字元， a - z, A - Z, 0 - 9, _
|   \W  | 匹配非文字字元

<br>

#### 符號 `.`

```python
>>> import re
>>> ret = re.match(".", "abc")
>>> ret.group()
'a'
```

<br>

#### 符號 `[]`

```python
>>> import re
>>> ret = re.match("[hH]", "hello Python")
>>> ret.group()
'h'
>>> ret = re.match("[0123456789]", "123 hello Python")
>>> ret.group()
'1'
>>> ret = re.match("[0-9]", "123 hello Python")
>>> ret.group()
'1'
```

<br>

#### 符號 `\d`

```python
>>> import re
>>> ret = re.match("Team No.\d","Team No.1")
>>> ret.group()
'Team No.1'
>>> ret = re.match("Team No.\d","Team No.2")
>>> ret.group()
'Team No.2'
```

<br><br>

### 原始字串

<br>

與大多數程式語言相同，正規表達式使用 `\` 作為轉義字元，轉義 `\` 就成了一個很大的困擾。 python 中的原生字串解決了這個問題，字串前加上 `r` 表示原生字串，不用擔心是否六寫了反斜線，而寫出來的正規表達式也更直觀

```python
>>> import re
>>> ret = re.match("\\a", "\a")
>>> ret.group()
'\x07'
>>> ret = re.match(r"\a", "\a")
>>> ret.group()
'\x07'
```

<br><br>

### 數量的匹配

<br>


| 符號   | 功能   |
| :---: | :---   |
|   *     | 匹配字元出現 0 次以上
|   +     | 匹配字元出現 1 次以上
|   ?     | 匹配字元出現 0 次或 1 次
|   {m}   | 匹配字元出現 m 次
|   {m,}  | 匹配字元出現 m 次以上
|   {m,n} | 匹配字元出現 m 次到 n 次


<br>

#### 符號 `*`

```python
>>> import re
>>> ret = re.match("[A-Z][a-z]*", "Aabcdef")
>>> ret.group()
'Aabcdef'
```

<br>

#### 符號 `+`

```python
>>> import re
>>> ret = re.match("[a-zA-Z_]+[\w_]*", "_name")
>>> ret.group()
'_name
```

<br>

#### 符號 `?`

```python
>>> import re
>>> ret = re.match("[1-9]?[0-9]", "0")
>>> ret.group()
'0'
>>> ret = re.match("[1-9]?[0-9]", "11")
>>> 
>>> ret.group()
'11'
```

<br>

#### 符號 `{m}`

```python
>>> import re
>>> ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
>>> ret.group()
'12a3g4
```

<br><br>

### 邊界的匹配

<br>

| 符號   | 功能   |
| :---: | :---   |
|   ^     | 匹配字串開頭
|   $     | 匹配字串結尾
|   \b    | 匹配單字元邊界
|   \B    | 匹配非單字元邊界

```python
>>> import re
>>> ret = re.match("^[\w]{4,20}@gmail\.com$","felix@gmail.com")
>>> ret.group()
'felix@gmail.com'
```

<br><br>

### 匹配的分組
<br>

| 符號   | 功能   |
| :---: | :---   |
|   \|           | 匹配左右任意6一個表達式 
|   (reg)         | 將括號中字串作為分組
|   \num         | 引用分組 num 批配到的字串
|   (?P\<name\>) | 將分組命名
|   (?P=name)    | 引用命名分組匹配到的字串

<br>

#### 符號 `|`

```python
>>> import re
>>> ret = re.match("[1-9]?[0-9]$|100","100")
>>> ret.group()
'100'
>>> ret = re.match("[1-9]?[0-9]$|100","0")
>>> ret.group()
'0'
>>> ret = re.match("[1-9]?[0-9]$|100","10")
>>> ret.group()
'10'
```

<br>

#### 符號 `(reg)`

```python
>>> import re
>>> ret = re.match("^(\w{4,20})@(gmail|yahoo|hotmail)\.com$","felix@gmail.com")
>>> ret.group()
'felix@gmail.com'
>>> ret.group(1)
'felix'
>>> ret.group(2)
'gmail'
```

<br>

#### 符號 `\num`

```python
>>> import re
>>> ret = re.match(r"<([a-zA-z]*)>[\w\s!]*</\1>","<html>hello world!</html>")
>>> ret.group()
'<html>hello world!</html>'
>>> ret.group(1)
'html'
```

```python
>>> import re
>>> ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>","<html><b>hello world!</b></html>")
>>> ret.group()
'<html><b>hello world!</b></html>'
>>> ret.group(1)
'html'
>>> ret.group(2)
'b'
```

<br>

#### 符號 `(?P<name>)` and `(?P=name)`

```python
>>> import re
>>> ret = re.match(r"<(?P<tag1>\w*)><(?P<tag2>\w*)>.*</(?P=tag2)></(?P=tag1)>","<html><b>hello world!</b></html>")
>>> ret.group()
'<html><b>hello world!</b></html>'
>>> ret.group(1)
'html'
>>> ret.group(2)
'b'
```

<br><br>

### `re` 模組的進階方法

<br>

#### search

```python
>>> import re
>>> ret = re.search(r"\d+", "read : 9999")
>>> ret.group()
'9999'
```

#### findall

```python
>>> ret = re.findall(r"\d+", "a=1 b=2 c=3 d=4")
>>> print(ret)
['1', '2', '3', '4']
```

#### sub

```python
>>> ret = re.sub(r"\d+", "10", "a=1 b=2 c=3 d=4")
>>> print(ret)
a=10 b=10 c=10 d=10
```

<br><br>

### 貪婪搜尋


