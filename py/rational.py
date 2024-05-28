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
