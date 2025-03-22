### 第001个知识点: .startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。

from xtquant import xtdata # 导入xtdata模块
import time # 导入time模块

.startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
all_stock_code = ['600000', '000004', '600006', '300007', '600008', '688009', '300010', '002211', '003212', '600015']

stock_code = '600'

for code in all_stock_code:
    if code.startswith(stock_code):
        print(code)

------------------------------------------------------------------------------------
### 第002个知识点: f-string 格式化字符串
f-string 是 Python 3.6 中引入的一种字符串格式化方式，允许在字符串字面值中直接嵌入表达式。

f"{}" 用于格式化字符串
price_list = [1.5126, 2.309, 3.547, 4.711233, 5.60999]
for price in price_list:
    print(f"{price:.2f}")

-----------------------------------------------------------------------------------
### 第003个知识点: format() 方法用于格式化字符串

{}.format() 用于格式化字符串
for price in price_list:
    print("{:.2f}".format(price))

for i in code_list:
i 是一个字符串，code_list 是一个列表，所以 i 会遍历 code_list 中的每一个元素

-------------------------------------------------------------------------------------
### 第004个知识点: 在命令行中查找端口号对应的 PID，并终止进程

'''
C:\\Users\ttyrc33>netstat -ano | findstr :58609
  TCP    127.0.0.1:58609        0.0.0.0:0              LISTENING       21460

C:\\Users\ttyrc33>taskkill /PID 21460 /F
成功: 已终止 PID 为 21460 的进程。
'''

--------------------------------------------------------------------------------
### 第005个知识点: git 常用命令

'''
检查当前状态
git status

添加所有更改的文件
git add .

提交更改
git commit -m "Initial commit"

添加远程仓库（如果还没有添加）
git remote add origin https://github.com/yourusername/yourrepository.git

推送到远程仓库
git push -u origin main'
'''

'''
`round` 函数用于将一个数字四舍五入到指定的小数位数。它的语法如下：

```python
round(number, ndigits)
```

- `number`：要四舍五入的数字。
- `ndigits`：要保留的小数位数。如果省略此参数，则默认四舍五入到整数。
'''

--------------------------------------------------------------------------
### 第006个知识点: round() 函数四舍五入

- 变量输入演练————超市买苹果增强版
1. 重量
2. 价格
3. 返回金额
4. 总价

- 重量
weight = float(input("请输入苹果的重量:"))

- 价格
price = float(input("请输入苹果的价格:"))

- 返回金额
money = float(input("请输入返回金额:"))

- 总价
total_price = weight * price - money
print(total_price)
print("{:.2f}".format(total_price))
print("%.2f" % total_price)
print(round(total_price, 2))
print(f"{total_price:.2f}")
print(type(total_price))

- 在这段代码中，round(total_price, 2) 将 total_price 四舍五入到小数点后2位，并输出结果。其他几种方法（format 方法、百分号格式化和 f-string）也可以实现相同的效果。


'''
要在固定空间内输出居中的字符串，可以使用 Python 的字符串格式化方法。虽然 `%` 格式化方法不支持居中对齐，但你可以使用 `str.center()` 方法来实现这一点。
以下是使用 `str.center()` 方法的示例：
'''

- 字符串格式化输出
s = 'www.baidu.com'
print("标准字符串输出:%s" % s)
print("固定空间输出右对齐:%20s" % s)
print("固定空间输出左对齐:%-20s" % s)
print("固定空间输出居中:%s" % s.center(20))
print("截取字符串输出:%.5s" % s)

'''
在这个示例中，`s.center(20)` 将字符串 `s` 居中对齐到 20 个字符的宽度。如果字符串长度不足 20 个字符，则在两侧填充空格。
输出结果如下：

标准字符串输出:www.baidu.com
固定空间输出右对齐:       www.baidu.com
固定空间输出左对齐:www.baidu.com       
固定空间输出居中:   www.baidu.com    
截取字符串输出:www.b

这样，你就可以在固定空间内居中对齐字符串了。
'''


'''
总结
在 Python 中，字符串是 str 类的实例，是不可变对象。
在 C++ 中，字符串是 std::string 类的实例，是可变对象。
两者都提供了丰富的方法和函数来操作字符串，但由于语言特性的不同，它们的实现和使用方式有所差异。
'''

'''
在 Python 中，% 格式化、str.format() 方法和 f-string 格式化的出现时间如下：

% 格式化：

这是最早的字符串格式化方法，类似于 C 语言中的 printf 风格。它在 Python 的早期版本中就已经存在。
str.format() 方法：

str.format() 方法是在 Python 2.6 和 Python 3.0 中引入的。它提供了一种更强大和灵活的字符串格式化方式，相比 % 格式化方法，str.format() 方法更易读和易用。
f-string 格式化：

f-string（格式化字符串字面值）是在 Python 3.6 中引入的。f-string 提供了一种更简洁和高效的字符串格式化方式，允许在字符串字面值中直接嵌入表达式。
时间顺序
% 格式化（最早）
str.format() 方法（Python 2.6 和 Python 3.0 引入）
f-string 格式化（Python 3.6 引入）
示例
以下是三种格式化方法的示例：

'''

- % 格式化
name = "Alice"
age = 30
print("Hello, %s. You are %d years old." % (name, age))

- str.format() 方法
print("Hello, {}. You are {} years old.".format(name, age))

- f-string 格式化
print(f"Hello, {name}. You are {age} years old.")

'''
每种方法都有其优点和适用场景，但 f-string 格式化由于其简洁性和高效性，通常是推荐的选择，特别是在 Python 3.6 及以上版本中。

'''

---------------------------------------------------------------------------
### 第007个知识点: enumerate() 函数


'''
当然可以！`enumerate` 函数用于将一个可迭代对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，通常用于在 `for` 循环中获取索引和值。

以下是一个简单的示例，展示了如何使用 `enumerate` 函数：
'''


- 示例字符串
str3 = "hello"

- 使用 enumerate 函数
for index, char in enumerate(str3):
    print(f"Index: {index}, Character: {char}")

'''
输出结果：

Index: 0, Character: h
Index: 1, Character: e
Index: 2, Character: l
Index: 3, Character: l
Index: 4, Character: o


在这个示例中，`enumerate(str3)` 返回一个枚举对象，该对象生成包含索引和值的元组。在 `for` 循环中，`index` 是字符的索引，`char` 是字符本身。

你也可以指定起始索引，默认情况下起始索引为 `0`。例如：
'''

- 示例字符串
str3 = "hello"

- 使用 enumerate 函数，指定起始索引为 1
for index, char in enumerate(str3, start=1):
    print(f"Index: {index}, Character: {char}")

'''
输出结果：

Index: 1, Character: h
Index: 2, Character: e
Index: 3, Character: l
Index: 4, Character: l
Index: 5, Character: o


在这个示例中，`enumerate(str3, start=1)` 将起始索引指定为 `1`。

你可以在你的代码中使用 `enumerate` 函数来获取字符串的索引和值：
'''

- 示例字符串
str3 = "hello"

- 打印 enumerate 对象的类型
print(type(enumerate(str3)))

- 使用 enumerate 函数
for index, char in enumerate(str3):
    print(f"Index: {index}, Character: {char}")

'''
这样，你就可以使用 `enumerate` 函数来遍历字符串并获取每个字符的索引和值。
'''

-------------------------------------------------------------------------------------------
### 第008个知识点: f-string 格式化中的负号显示

'''
在 Python 的 f-string 格式化中，`-` 标志用于左对齐，而不是用于显示负号。要显示负号，你可以直接在格式化字符串中使用 `+` 标志，这样正数会显示 `+` 号，负数会显示 `-` 号。

以下是修正后的代码示例：

```python
number_pi = 3.1415926
number_1 = 123
number_2 = 123456789
number_3 = 0.123
number_4 = -1

print(f"{number_pi:.2f}")   # 输出: 3.14
print(f"{number_pi:+.2f}")  # 输出: +3.14
print(f"{number_pi:.0f}")   # 输出: 3
print(f"{number_4:+.0f}")   # 输出: -1
```

在这个示例中：

- `f"{number_pi:.2f}"` 将 `number_pi` 格式化为保留两位小数的浮点数。
- `f"{number_pi:+.2f}"` 将 `number_pi` 格式化为保留两位小数的浮点数，并显示正负号。
- `f"{number_pi:.0f}"` 将 `number_pi` 格式化为不保留小数的浮点数。
- `f"{number_4:+.0f}"` 将 `number_4` 格式化为不保留小数的浮点数，并显示正负号。

这样，你就可以正确地显示负号了。
'''

 -------------------------------------------------------------------------------------
### 第009个知识点: 函数嵌套调用

'''
是的，函数嵌套调用就是在一个函数中定义和调用另一个函数。在你的示例中，`sum_and_subtract` 函数中定义了两个嵌套函数 `sum_two_numbers` 和 `subtract_two_numbers`，并在 `sum_and_subtract` 函数中调用它们。

以下是你的代码示例：
'''

- 函数的嵌套调用
```python
def sum_and_subtract(a, b):
    def sum_two_numbers(a, b):
        return a + b
    def subtract_two_numbers(a, b):
        return a - b
    sum_result = sum_two_numbers(a, b)
    subtract_result = subtract_two_numbers(a, b)
    return sum_result, subtract_result

result = sum_and_subtract(11, 22)
print(result)
```

'''
在这个示例中：

1. `sum_and_subtract` 函数接受两个参数 `a` 和 `b`。
2. 在 `sum_and_subtract` 函数内部，定义了两个嵌套函数：
   - `sum_two_numbers(a, b)`：计算 `a` 和 `b` 的和。
   - `subtract_two_numbers(a, b)`：计算 `a` 和 `b` 的差。
3. 在 `sum_and_subtract` 函数中，调用 `sum_two_numbers(a, b)` 和 `subtract_two_numbers(a, b)`，并将结果分别赋值给 `sum_result` 和 `subtract_result`。
4. `sum_and_subtract` 函数返回一个包含 `sum_result` 和 `subtract_result` 的元组。
5. 调用 `sum_and_subtract(11, 22)` 并将结果赋值给 `result`，然后打印 `result`。

输出结果：

```
(33, -11)
```

嵌套函数的主要用途包括：

- **封装逻辑**：将相关的逻辑封装在一个函数内部，使代码更易读和维护。
- **作用域控制**：嵌套函数只能在其外部函数内部访问，避免了命名冲突和不必要的全局命名空间污染。
- **闭包**：嵌套函数可以访问其外部函数的变量，这在某些情况下非常有用，例如实现装饰器或回调函数。

总之，函数嵌套调用是一种在函数内部定义和调用其他函数的技术，用于提高代码的组织性和可维护性。
'''

--------------------------------------------------------------------------------------------
### 第010个知识点: 类中的实例方法、类方法和静态方法


'''
在 Python 中，类方法和静态方法提供了不同的功能和用途，它们在设计类时具有特定的好处。以下是对类方法和静态方法的详细解释及其好处：

#### 实例方法

实例方法是最常见的方法类型，它们的第一个参数是 `self`，表示类的实例。实例方法可以访问和修改实例属性和类属性。

```python
def study(self, course_name):
    print(f'{self.name}正在学习{course_name}, {self.name}今年{self.age}岁')
```

#### 类方法

类方法的第一个参数是 `cls`，表示类本身，而不是类的实例。类方法使用 `@classmethod` 装饰器来定义。类方法可以访问和修改类属性，但不能直接访问实例属性。

#### 好处：

1. **访问类属性**：类方法可以访问和修改类属性，这对于需要在类级别上操作数据的方法非常有用。
2. **工厂方法**：类方法常用于实现工厂方法，工厂方法是一种创建类实例的替代构造器。

```python
@classmethod
def get_count(cls):
    return cls.count
```

#### 静态方法

静态方法不需要表示实例或类的参数（即没有 `self` 或 `cls` 参数）。静态方法使用 `@staticmethod` 装饰器来定义。静态方法不能访问或修改类属性和实例属性。

#### 好处：

1. **逻辑分组**：静态方法用于将一些逻辑上相关的函数放在类的命名空间中，即使它们不需要访问类或实例的属性。
2. **实用工具**：静态方法通常用于实现一些实用工具函数，这些函数与类相关，但不需要访问类或实例的属性。

```python
@staticmethod
def plus(a, b):
    return a + b
```

#### 示例

以下是一个包含实例方法、类方法和静态方法的完整示例：
'''

### 创建一个学生类
```python
class Student:
    # 类属性
    count = 0

    # 构造方法
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age
        # 类属性
        Student.count += 1

    # 实例方法
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}, {self.name}今年{self.age}岁')

    # 静态方法
    @staticmethod
    def plus(a, b):
        return a + b

    # 类方法
    @classmethod
    def get_count(cls):
        return cls.count

# 创建学生实例
student1 = Student('Alice', 20)
student2 = Student('Bob', 21)

# 调用实例方法
student1.study('数学')
student2.study('英语')

# 调用静态方法
result = Student.plus(11, 22)
print(f"11 + 22 = {result}")

# 调用类方法
count = Student.get_count()
print(f'学生总数为: {count}')
```

'''
### 总结

- **实例方法**：用于操作实例属性和类属性。
- **类方法**：用于操作类属性，常用于工厂方法和类级别的操作。
- **静态方法**：用于逻辑分组和实用工具函数，不需要访问类或实例的属性。

通过使用实例方法、类方法和静态方法，可以更好地组织代码，明确不同方法的用途和作用范围，提高代码的可读性和可维护性。
'''

-------------------------------------------------------------------------------------------
### 第011个知识点: 

'''


'''