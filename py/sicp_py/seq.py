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
