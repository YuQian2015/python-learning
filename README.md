## 开始

### 为什么学习Python

- 使用场景：自动化、人工智能、应用、网站
- 最简单的编程语言
- 非常受欢迎的编程语言
- Python岗位和待遇

### 下载Python

- 访问 https://www.python.org/downloads/
- 点击下载按钮下载
- 打开下载的文件
- 勾选添加到PATH
- 点安装，完成

### IDE选择

- [PyCharm](https://www.jetbrains.com/pycharm/ )，可以下载社区免费版
- 点击下载社区版
- 打开下载的文件
- 可以勾选64位版启动
- 建议开启添加PATH
- 下一步，安装
- 打开 PyCharm ，点击创建项目
- 选择项目地址，填写项目名称
- 点击创建
- 如果勾选创建 main.py ，编辑器会自动生成一部分代码在文件里面，也可以删除之后进行编程

### 第一个Python程序

使用 `print()` 可以输出一段字符，可以使用 `'` 或者 `"` 来包含字符，点击 IDE 上的运行按钮可以看到输出：

```python
print('Hello World!')
# 输出结果：Hello World!

print('a' * 10)
# 输出结果：aaaaaaaaaa
```

## 变量

变量是一些值的存储容器，变量支持各种类型，Numbers、String、List、Tuple、Dictionary

- Numbers（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Dictionary（字典）

### 定义变量

使用变量可以在电脑内存中存储数据，比如下面的代码，定义了一个变量叫 `price` ，并且将一个数字10存储在里面：

```python
price = 10
print(price)
# 输出结果：10
# 不能使用 print('price')，这将输出一串字符
```

当 Python 执行变量定义时，使用计算机内存并以二进制存储数据，变量会指向数据被存储的位置。

### 检查变量类型

使用 `type()` 方法检查变量的类型：

```python
name = "Bro"
print(type(name))
# 输出结果：<class 'str'>
```

### 变量赋值

```python
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
is_published = True  # 布尔型
print(counter)
print(type(counter))
print(miles)
print(type(miles))
print(name)
print(type(name))
print(is_published)
print(type(is_published))
# 输出结果：
# 100
# <class 'int'>
# 1000.0
# <class 'float'>
# John
# <class 'str'>
# True
# <class 'bool'>


a = b = c = 1
```

Python 是大小写敏感的语言，因此在定义变量时，可以使用小写字母，单词之间使用下划线连接，但是布尔值 `True` 和  `False` 这一类关键字是大写开头的。上面的代码中的变量赋值都属于简单值，Python 也支持复杂的赋值方式。

### 接收输入

使用 `input()` 函数可以接收用户输入的字符串：

```python
name = input('What is your name? ')
print('Hi ' + name)
```

### 类型转换

有如下代码，要求输入生日，当输入成功之后，将计算年龄：

```python
year = input('输入生日： ')
age = 2021 - year
print(age)

# 执行错误：
Traceback (most recent call last):
  File "F:/project/python-learning/main.py", line 2, in <module>  # 出错的文件和行数
    age = 2021 - year  # 出错的代码
TypeError: unsupported operand type(s) for -: 'int' and 'str'  # 出错的原因

# 修改之后
year = input('输入生日： ')
age = 2021 - int(year)
print(age)
```

Python 预置了一些函数来进行类型转换：

- `int()` - 转换成整形
- `float()` - 转换成浮点型
- `bool()` - 转成布尔型

## 字符串

### 字符串定义

```python
course = "Python's Course for Beginners"  # 显示单引号
course2 = 'Python for "Beginners"'  # 显示双引号
course3 = 'Python\'s Course for Beginners'  # 显示单引号

print(course)
# 输出结果：Python's Course for Beginners
print(course2)
# 输出结果：Python for "Beginners"
print(course3)
# 输出结果：Python's Course for Beginners

```

### 根据index获取字符串

```python
course = "Python's Course for Beginners"  # 显示单引号
course2 = 'Python for "Beginners"'  # 显示双引号
course3 = 'Python\'s Course for Beginners'  # 显示单引号

print(course[0])  # 获取第一个字符
print(course[-1])  # 获取倒数第一个字符
print(course[0:3])  # 获取第一个到第三个字符，不包含course[3]
print(course[1:])  # 获取从第二个到最后一个的字符串
print(course[:5])  # 获取前五个字符, 相当于print(course[0:5])
print(course[:])  # 相当于复制一个字符串
# 输出结果：
# P
# s
# Pyt
# ython's Course for Beginners
# Pytho
# Python's Course for Beginners


name = 'Jennifer'
print(name[1:-1])
# 输出结果：ennife
```

### 多行字符串

```python
# 显示多行文本
email = '''
Hi John,

Here is out first email to you.

Thank you,
The support team

'''
print(email)
# 输出结果：
# Hi John,
# 
# Here is out first email to you.
# 
# Thank you,
# The support team
# 
```

如果想要使用变量动态的更改一串字符的内容，使用格式化字符串将会非常有效，使用方式就是用 `f''` 包含你的字符串，然后使用 `{}` 来插入变量：

```python
firstname = 'John'
lastname = 'Smith'

message = firstname + ' [' + lastname + '] is a coder'
msg = f'{firstname} [{lastname}] is a coder'

print(message)
print(msg)
# 输出结果：
# John [Smith] is a coder
# John [Smith] is a coder
```

字符串长度：

```python
course = 'Python for Beginners'
print(len(course))
# 输出结果：20
```

`len()` 是 Python 内建的一个函数，可以用来计算字符串的长度，或者计算数组的长度。

### 字符串方法

- `upper()` - 转大写，返回新的字符串
- `lower()` - 转小写，返回新的字符串
- `find()` - 查找字符，返回字符所在的index
- `replace()` - 替换字符，返回新的字符串
- `in` - 判断字符串是否存在，返回布尔值

```python
course = 'Python for Beginners'
print(course.upper())
# 输出结果：PYTHON FOR BEGINNERS

print(course.lower())
# 输出结果：python for beginners

print(course.find('P'))
print(course.find('o'))
print(course.find('O'))
print(course.find('Beginners'))
# 输出结果：
# 0
# 4
# -1
# 11

print(course.replace('Beginners', 'Absolute Beginners'))
# 输出结果：Python for Absolute Beginners
print(course.replace('beginners', 'Absolute Beginners')) # 替换不会生效，大小写需要匹配

print('Python' in course)
# 输出结果：True
print('python' in course)
# 输出结果：False

print(course)
# 输出结果：Python for Beginners
```

上面的方法不会修改原字符串，而是创建了新的字符串。

## 运算符

### 运算符号

- `+` - 加法
- `-` - 减法
- `*` - 乘法
- `/` - 除法
- `//` - 除法并获取整数部分
- `%` - 获取余数
- `**` - 次方

```python
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
# 输出结果：
# 13
# 7
# 30
# 3.3333333333333335
# 3
# 1
# 1000

x = 10
x = 10 + 3
print(x)
# 输出结果：13

x = 10
x += 3
print(x)
# 输出结果：13
```

### 运算优先级

运算符优先级，次方最高、乘除其次、加减最低，括号 `()` 里面的运算优先：

```python
print(10 + 3 * 2 ** 2)
# 输出结果：22

print((10 + 3) * 2 ** 2)
# 输出结果：52
```

### 运算函数

Python内建的函数和math模块，Python中的模块就是单独的可重复利用的代码：

```python
import math
print(round(2.9))
print(round(2.5))
print(abs(-2.5))

print(math.floor(2.5))
print(math.ceil(2.5))
# 输出结果：
# 3
# 2
# 2.5
# 2
# 3
```

