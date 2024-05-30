from operator import add

def count(s, value):
    total, index = 0, 0
    # while index < len(s):
    #     if s[index] == value:
    #         total += 1
    #     index += 1

    # 一个更好的写法是
    for elem in s:
    # 从可迭代的s中依次取出值并绑定在elem上
    # for执行完毕之后，环境中的elem绑定在s的最后一个迭代值
        if elem == value:
            total += 1

    # 可以使用range和list来创建序列
    # >>> list(range(5))
    # [0, 1, 2, 3, 4]
    # >>> for _ in range(i)
    # 仅仅用作重复，变量默认为_

    return total

# 列表推导式的一个示例，将奇数转换成偶数
odds = [1, 3, 5, 7, 9]
print([x+1 for x in odds])

# 列表推导式还可以用来选择列表中的值
print(x for x in odds if 25 % x == 0)

# 可以将序列中的所有值聚合为一个值
# 下面用这种方式求出 n 的完美数，即等于其约数之和的正整数

def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def perfect(n):
    return [x for x in range(1, n) if sum(divisors(x)) == x]

print(perfect(1000))

# 求固定面积矩形的最小周长
def width(area, height):
    assert area % height == 0 # 保证边长是整数，否则会报错
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

print(minimum_perimeter(80))

# 高阶函数是另一种常见的设计模式
def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

# 聚合相当于将双函数参数重复应用到 reduced 值
def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

# 下面给出一种利用高阶函数寻找完美数的方法
def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))
def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == 0

# 继续扩展序列抽象

# membership
digits = [1, 8, 2, 8]
print(2 in digits)
# True

# slicing
# >>> digits[起始索引: 结束索引+1: 步长]
print(digits[::-1])
# [8, 2, 8, 1]

# 利用列表创建层次结构，以树为例
def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

# 构造
t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])

# 树递归可用于构造树
def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])
    
print(fib_tree(5))