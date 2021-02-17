# 多分支结构

from random import *
import calendar
import math
a = 2

if a == 1:
    print('a == 1')
elif a == 2:
    print('a == 2')
else:
    print('a~~')

0.2 == 0.3

0.3 == 0.1+0.2

a = 0.1 + 0.2

abs(a-0.3) < 0.000001


math.isclose(a, 0.3)


# 多条件语句

a = 3

a > 2 and a < 4  # True

5 > a > 2

2 < a < 5

2 < a > 5


a = 1 or 2
print(a)

# 判断是否闰年

calendar.isleap(1)

# 分支单行表示

print('avc{}'.format('111'+'222'))


a = input('请输入：')
print('用户输入{}'.format(a))


# zip

names = ['小明', '小红']
ages = [12, 19]
for name, age in zip(names, ages):
    print('{}今年{}'.format(name, age))


# random

# import random


seed(12)

a = "{}-{}-{}".format(randint(2, 111), randint(1, 10), randint(1, 10))
print(a)


## 错误捕捉

try:
    num = eval(input('请输入一个整数：'))
    print(num**2)
    raise Exception # 主动报错，但是不会走到 NameError
except NameError as type1:
    print('输入错误，请输入一个整数',type1)
except:
    print('未知类型错误')
else:
    print('输入正确')
finally:
    print('怎么样都会走到这里')


# 要求使用try...except...else...finally 编写一个用户密码输入程序，要求全部为数字，要求长度8位，不符合要求时抛出异常，可以用 raise 方法

for nun in range(3):
    age = input('请输入数字年龄：')
    try:
        if int(age) !=  18:
            print('很遗憾没猜对')
            continue
        else:
            print('恭喜你猜对了')
            break
    except:
        print('请输入正确的类型')

# 要求使用try...except...else...finally 编写一个用户密码输入程序，要求全部为数字，要求长度8位，不符合要求时抛出异常，可以用 raise 方法

try:
    account = eval(input('请输入账号'))
    password = eval(input('请输入密码'))
    if not(type(account) is int and type(password) is int ):
        raise TypeError('账号或密码须为数字')
    elif not(len(str(account)) == 8 and len(str(password)) == 8):
        raise ValueError('账号或密码长度必须为8位')
except TypeError as msg:
    print(msg)
except ValueError as msg:
    print(msg)
except:
    print('未知类型')
else:
    print('输入正确')
finally:
    print('退出')


# 函数

# 默认值
def repeat(str='',name='',age=''):
    print(str,name,age)

repeat('123','xiaoming',15)

# 可变参数*
def func(x,*y):
    print(x,max(y))

func(1,2,3,4,5)

# 传参时扩展
def func2(x,*y):
    print(x,*y)

func2((1,2,3))

# 函数充当参数

def func3(fun):
    return fun()
def func4():
    print('func4')
func3(func4)

# 多个返回值

def move(x,y):
    return x,y
resX,resY = move(1,2)
print(resX,resY)

# 函数嵌套

def fn1():
    def fun2():
        return
    def fun3():
        return
    def fun4():
        return
    return

# 局部变量和全局变量

sideNum = 1
def sideNumFn():
        print(sideNum)
sideNumFn()

def func5():
    global sideNum
    sideNum = 2

func5()
print(sideNum)


# lambda

c = lambda x,y,z:x+y+z
print(c(1,2,3))

# map

