# Python字符串、列表、字典、元组、集合
# String
* Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points.
* Python中的文本数据是通过str对象或字符串来处理的，字符串是由一系列Unicode码位（code point）所组成的不可变序列
* Unicode 暂时可以看作一张非常大的地图，这张地图里面记录了世界上所有的符号，而码位则是每个符号所对应的坐标。(ascii)
* Python允许空字符串''，它不包含任何字符但完全合法。空字符串是其他任何字符串的子串。
* 字符串字面量是一个单独的表达式，如果多个字符串字面量中间仅包含空白，则它们将被隐性地转换为一个单一的字符串字面量。所以，("spam" "eggs") == "spameggs"。
* 常见的转义符：\n（换行符）、\t（Tab制表符）、\'（单引号）、\"（双引号）、\\（反斜线）
## ascll码 与 字符 之间转换函数
* chr() 接受一个整数，返回对应的Unicode字符
* ord() 功能与chr() 相反

```python
print(ord('我'),' ',ord('喜'),' ',ord('欢'),' ',ord('你'))
# 25105   21916   27426   20320
print(chr(25105),chr(21916),chr(27426),chr(20320))
# 我 喜 欢 你
```
### string一些常用方法
* split() 基于分隔符将字符串分割成由若干子串组成的列表，如果不指定分割符，默认使用空白字符进行分割。
* join() 与split()功能相反，将包含若干子串的列表分解，并将这些子串通过指定的粘合用的字符串合并成一个完整的大的字符串。
* find() 查找返回字符串中第一次出现子串的位置（偏移量），失败时返回-1。
* index() 与find()类似，但是查找失败时将触发ValueError异常。
* rfind() 与find()类似，但返回最后一次子串出现的位置。
* startswith() 判断字符串是否以特定前缀开头。
* endswith() 判断字符串是否以特定后缀结尾。
* count() 统计子串在字符串中出现的次数。
* is* 判断字符串中字符是否符合某种类型或者规则。
* strip() 返回移除开始和结尾空白字符的字符串，如果指定参数，将在字符串的开始和结尾移除参数中所包含的字符。
* upper() lower() swapcase() 分别将字符串所有字母转换成大写、转换成小写、大小写转换。
* title() 将字符串中所有单词的开头字母变成大写。
* capitalize() 将字符串首字母变成大写。
* center() ljust() rjust() 分别将字符串根据指定长度居中对齐、左对齐、右对齐。
* replace() 进行简单的子串替换，需要传入的参数：需要被替换的子串，用于替换的新子串，以及需要替换多少处。

# 列表
* 列表是最常用的Python数据类型，其非常适合利用顺序和位置定位某一元素，而且其元素不需要类型相同。列表是可变的，可以直接对原始列表进行修改：添加、删除、覆盖元素。列表中具有相同值的元素允许出现多次。
### 创建列表
* 只要把逗号分隔的不同的数据项使用方括号（[]）括起来即可。或者使用内置的list()函数。
### list一些常用函数
* 使用 append() 函数在列表的末尾添加元素
* 使用insert()函数在指定位置插入元素，其接受两个参数，第一个参数指定要插入的位置（偏移量），第二个参数指定要插入的元素。如果指定的偏移量超过了列表的尾部，则插入到列表最后。
* 通过索引（偏移量）访问某列表元素，并可以通过赋值操作对其进行修改
* 使用del删除指定位置的元素，当列表中的元素被删除后，位于其后面的元素自动迁移填补空位，且列表长度减去删除的元素个数。
* 使用remove()删除具有指定值的元素：
* 使用pop()可以获取列表中指定位置的元素，并将此元素从列表中删除。如果未指定参数，则默认返回列表末尾的元素，使用pop(0)将返回列表头部的元素。当列表为空或者索引超出范围时，将触发IndexError异常。
* * 这里我感觉可以参考栈的一些思想，能更好的理解
* 使用clear()函数清空列表中的所有元素：
* 使用extend()函数或+=操作合并列表：
* 使用index()函数查询具有特定值的元素在列表中的位置（偏移量）
* 使用in判断元素是否包含于某个列表中。
* 使用count()记录特定值在列表当中出现的次数。
* 排序
* * 使用列表对象方法sort()对原列表进行排序，改变原列表内容。
* * 使用通用函数sorted() 返回排好序的列表副本，原列表内容不变。
* * test

```python
nums = [10,5,6,9,1,2,8,7,66]
nums1 = sorted(nums)
print(nums)
print(nums1)

# 正序
nums.sort()
print(nums)
# 倒序
nums.sort(reverse=True)
print(nums)
```
* * * 运行结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200630185914400.png)
* 复制列表
* * 列表copy()函数
* * list()转换函数
* * 列表切片[:]
# 元组
* 元组与列表有很多相似之处，但它是一种不可变的容器。
* 元组一旦被定义以后，将无法再进行添加、删除或修改元素等操作。
* 它能用来做一些列表不能做的事，如用作一个字典的键。
* 鉴于其与列表很大程度上是相似的，所以这里着重描述元组和列表的不同之处。
## 创建元组
*  元组用()或工厂函数tuple()。（列表用[]或工厂函数list(））
## 元组解包
* 将元组赋值给多个变量，这个过程可被称作元组解包。

```python
list = [1,22,333]
yz = tuple(list)
print(yz)# (1, 22, 333)
a,b,c= yz
print(a,b,c) # 1 22 333
```
* 元组的不变，是指tuple的每一个元素的指向永远不变。（但是可以采用浪费空间的方法，创建一个新的需要的元组）

# 字典
* 字典（dictionary）是Python中唯一的“映射”类型，映射这个概念在高中就学过：
一个函数f将键（key，定义域）映射到值（value，值域）。
这样的函数在字典中可以称为哈希（HASH）函数。
通过哈希函数可以对键通过计算快速得到值的位置，而避免了线性搜索，
极大的提高了数据值的存取效率；此外，字典是容器类型，可更新模型。
基于这些特性，字典通常被认为是Python中最强大的数据类型之一。
* * 简单来说key值是惟一的，value可以存在多个
* 字典中的键通常是字符串，但还可以是Python中其他任意的不可变对象：
布尔型、整型、浮点型、元组等。
## 创建和赋值
* 使用{}创建空字典。使用dict()构造器可从其他对象创建字典。
* code

```python
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
dict(lol)  ==> {'a': 'b', 'c': 'd', 'e': 'f'}

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
dict(lot)  =⇒ {'a': 'b', 'c': 'd', 'e': 'f'}

tol = (['a','b'], ['c', 'd'], ['e', 'f'])
dict(tol)  ==> {'a': 'b', 'c': 'd', 'e': 'f'}

los = ['ab', 'cd', 'ef']
dict(los)  ⇒ {'a': 'b', 'c': 'd', 'e': 'f'}

tos = ('ab', 'cd')
dict(tos)  ⇒ {'a': 'b', 'c': 'd'}
```
##### 其实也没什么了，还有字典常用的连个函数

```python
dic = {}
dic.keys()
dic.values()
```

# 集合
* Python中的集合有两种类型，可变集合（set）和不可变集合（frozenset），对于可变集合，可以添加和删减元素，但不可哈希，因此不能用作字典的键，也不能作为其它集合的元素；而不可变集合可以哈希，可以被用作键或者集合成员。
## 创建集合
* 使用大括号将一系列以逗号隔开的值包裹起来就创建了一个集合，另外可以使用内建的set()和frozenset()构造器创建集合。
## 集合类型操作符和内建方法
### 标准类型操作符
* 1、成员关系判定：in、not in
* 2、集合等价/不等价： ==、!=
* 3、子集/超集判定： <、<=、>、>=
### 集合类型的内建方法
* 这里我建议死记硬背，Python很多方法都是互通的（争取举一反十，哈哈``）

```python
# 用于所有集合的方法
s.issubset(t)            # 如果s是t的子集，返回True
s.issuperset(t)          # 如果s是t的超集，返回True
s.union(t)               # 返回一个新集合（s和t的并集）
s.intersection(t)        # 返回一个新集合（s和t的交集）
s.difference(t)          # 返回一个新集合（s - t）
s.symmetric_difference(t)
                         # 返回一个新集合（s ^ t）
s.copy()                 # 返回一个新集合，它是s的浅复制

# 仅用于可变集合的方法
s.update(t)              # 用t中的元素更新s
s.intersection_update(t) # s中现在是s和t的交集
s.difference_update(t)   # s中现在是（s - t）
s.symmetric_difference_update(t)
                         # s中现在是s和t异或的结果
s.add(obj)               # 在s中添加对象obj
s.remove(obj)            # 从s中删除对象obj，如果不存在则引发KeyError异常
s.discard(obj)           # 如果obj是s的元素，就从s中删除
s.pop()                  # 删除s中任意一个对象，并返回
s.clear()                # 删除集合s中的所有元素
```

###### ps: 由于一些知识点过于基础,所以会一些编程题的形式呈现出来
* Python中7个序列的内置类型（列表，元组，range，str，bytes，bytearray，memoryview）
## 字符串与字典
### 用户输入一个数字，打印这个数字出现的每一位数字的次数

```python
# 用户输入一个数字，打印这个数字出现的每一位数字的次数
# 用户输入一个数字，打印这个数字出现的每一位数字的次数

def find_num_counts():
    nums = input()
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1

    for k in dic.keys():
        print(f"{k} 出现 {dic[k]} 次")

find_num_counts()
```
#### 运行结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200630180936802.png)
### 将列表[1,3,2,5,4,1,2,3,6,8,4,2]中的重复元素去掉并排好序（分别打印正序和倒叙）
* set() : 可以将列表变成集合（去掉重复元素，并且将元素按照从小到大的排序进行排序）

```python
def deal_list():
    list_=[1,3,2,5,4,1,2,3,6,8,4,2]
    l1 = list(set(list_))
    print('正序：',l1)
    print('倒叙：',l1[::-1])

deal_list()
```
#### 运行结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200630182014575.png)
### 存在一个列表list = [{'id' : 1,'name' : 'zhangsan','age' : '1'},{'id' : 2,'name' : 'lisi','age' : '2'}],请设计实现：用户输入姓名，返回对应年龄,如果姓名不在内，则输出Not Found。

```python
def find_user():
    name = input()
    list = [{'id' : 1,'name' : 'zhangsan','age' : '1'},{'id' : 2,'name' : 'lisi','age' : '2'}]
    is_exist = False
    for i in range(len(list)):
        if list[i]['name']==name:
            is_exist=True
            print(f'{name} 的年龄为 {list[i]["age"]}')
    if not is_exist:
        print("Not Found")

find_user()
find_user()
```
#### 运行效果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200630182747565.png)
## 浅拷贝与深拷贝（重点）
### 浅拷贝
* 将对象中的第一级对象的引用进行拷贝
### 深拷贝
* 将对象中的所有层级的子对象的引用进行拷贝
### 总结
* 浅拷贝与深拷贝都是在拷贝引用地址二不拷贝值，区别在于拷贝的层级不一样‘
* python中，万物皆对象
* “=”就是复制对象的引用
## 这里我们详细介绍下Python 中的 copy
* 当然啦，可以看手册了啦：https://docs.python.org/zh-cn/3/library/copy.html
### copy --- 浅层 (shallow) 和深层 (deep) 复制操作
* Python 中赋值语句不复制对象，而是在目标和对象之间创建绑定 (bindings) 关系。对于自身可变或者包含可变项的集合对象，开发者有时会需要生成其副本用于改变操作，进而避免改变原对象。本模块提供了通用的浅层复制和深层复制操作（如下所述）。
* copy.copy(x)
* * 返回x的浅层复制
* * A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.

* copy.deepcopy(x[, memo])
* * 返回x的深层复制
* * A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

* 制作字典的浅层复制可以使用 dict.copy() 方法，而制作列表的浅层复制可以通过赋值整个列表的切片完成，例如，copied_list = original_list[:]。

### 小记
* 2020.06.30 19:15
* 对自己的要求，合理安排时间打王者荣耀，不要一玩就一直玩下去，直到手机没电，晚上的时候，把手机放在父母的房间，吃完饭后坚决不碰


