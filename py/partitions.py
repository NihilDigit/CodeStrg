def count_partitions(n, m):
    """计算 n 的分割数，数字中最大者为 m """
    """To be clear, 其实我没理解这些是什么玩意"""
    if n == 0:
        return 1 
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    #定义了递归中止基线，n<=0或者最大分割数字是0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)
        #把问题分解到(n-m, m)和(n, m-1)，即至少包含一个m的和一个m都不包括的