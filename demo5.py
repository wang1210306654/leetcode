"""
@auth whs
@time 2020-06-10
@name 爬楼梯
@info 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
@param n int 楼梯阶数
@param i int 当前阶数
"""
"""
暴力破解 + 记忆化递归
假设有4阶
解1：
当在(0,4),可分为(1,4),(2,4)两种,意思是可以登上1阶或者2阶
当在(2,4),可分为(3,4),(4,4)两种,意思是可以登上1阶或者2阶
当在(3,4),可分为(4,4),(5,4)两种,意思是可以登上1阶或者2阶
当为(5,4),数据无效,当为(4,4),为最后一次登阶。
                                (0,4)
                (1,4)                      (2,4)
        (2,4)       (3,4)        (3,4)        (4,4)
    (3,4)(4,4)(4,4)(5,4)(4,4)(5,4)
(4,4)(5,4)
"""
def fun1(i,n,cache):
    #####################
    # 记忆化递归
    # fun1(0,n,{})
    if i in cache:
        return cache[i]
    if i == n:
        return 1
    if i > n:
        return 0
    cache[i] = fun1(i+1,n,cache) + fun1(i+2,n,cache)
    return cache[i]
    ###################################
    # fun1(0,n)
    # if i == n:
    #     return 1
    # if i > n:
    #     return 0
    # return fun1(i+1,n) + fun1(i+2,n)

"""
解2：自上而下---动态规划
            (4,4)
      (3,4)       (2,4)
  (2,4)   (1,4)(1,4)(0,4)
(1,4)(0,4)(0,4)(0,4)  1
(0,4)  1    1    1
  1    
当在(4,4)，是从(3,4)或(2,4)上去的，方法数量是(3,4)+(2,4)
当在(3,4)，是从(2,4)或(1,4)上去的，方法数量是(2,4)+(1,4)
当在(2,4)，是从(1,4)或(0,4)上去的，方法数量是(1,4)+(0,4)
当在(1,4)，是从(0,4)上去的
(0,4)到上面一层只有一种方法
(4,4)

第 i 阶可以由以下两种方法得到：
    在第 (i-1)(i−1) 阶后向上爬一阶。
    在第 (i-2)(i−2) 阶后向上爬 22 阶。
所以到达第 i 阶的方法总数就是到第 (i-1) 阶和第 (i-2) 阶的方法数之和。
令 dp[i] 表示能到达第 i 阶的方法总数：
dp[i]=dp[i-1]+dp[i-2]
"""
def fun2(n):
    df = {}
    df[1] = 1
    df[2] = 2
    for i in range(3,n+1):
        df[i] = df[i-1] + df[i-2]
    return df[n]

"""
解法三：斐波那契数
根据上边的自上而下，可以得到，第i个就是等于i的斐波那契数
把i i-1 i-2 .... 个斐波那契数相加，就是值
"""
def fun3(n):
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in range(3,n+1):
        third = first + second
        first ,second = second ,third
    return second

if __name__ == '__main__':
    n = 100
    print(fun3(n))
    