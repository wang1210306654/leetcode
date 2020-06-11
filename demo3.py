"""
@auth whs
@time 2020-06-10
@name 杨辉三角/帕斯卡三角形
@info 帕斯卡三角形是排列成三角形的一系列数字。 在帕斯卡三角形中，每一行的最左边和最右边的数字总是 1。
        对于其余的每个数字都是前一行中直接位于它上面的两个数字之和。
@param n int 行数
"""
def triangle(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    upper = triangle(n - 1)
    tmp = []
    tmp.append(1)
    for i in range(1, n - 1):
        tmp.append(upper[-1][i - 1] + upper[-1][i])
    tmp.append(1)
    upper.append(tmp)
    return upper


if __name__ == '__main__':
    n = 30
    re = triangle(n)
    print(re)

