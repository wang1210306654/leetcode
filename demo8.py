"""
@auth whs
@time 2020-06-11
@name 泰波那契数
@info 泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
@param n
"""
def tribonacci(n,cache):
    if n <= 0 : return 0
    if n == 1 : return 1
    if n == 2 : return 1
    if n in cache:
        return cache[n]
    cache[n] = tribonacci(n - 1,cache) + tribonacci(n - 2,cache) + tribonacci(n - 3,cache)
    return cache[n]

class Solution:
    def tribonacci(self, n: int) -> int:
        return self.do(n,{0:0,1:1,2:1})

    def do(self,n,cache):
        if n < 0 : return 0
        if n in cache:
            return cache[n]
        cache[n] = self.do(n - 1,cache) + self.do(n - 2,cache) + self.do(n - 3,cache)
        return cache[n]

if __name__ == '__main__':
    # print(tribonacci(4,{}))
    a = Solution()
    print(a.tribonacci(4))