from fractions import gcd

# 创建/操作有理数

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def rational(n, d):
    g = gcd(n, d) #greatest common denominator
    return (n//g, d//g)

# 使用有理数进行计算

def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

# 抽象屏障

def square_rational(x):
    return mul_rationals(x, x)

def square_rational_violating(x):
    return rational(numer(x) * numer(x), denom(x) * denom(x))

# 第二种写法就违反了抽象屏障，访问numer的行为实际上跨越了两层抽象
# 保证抽象屏障可以增强代码的可维护性，我们可以在不损坏其他函数的情况下改变有理数的表示方式
