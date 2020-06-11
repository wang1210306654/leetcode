"""
@auth whs
@time 2020-06-10
@name 斐波那契数
@info 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和
@param n int
"""
def fib(n,cache):
    res = 0
    if n in cache:
        return cache[n]
    if n < 2:
        print(n)
        res = n
    else:
        res = fib(n-1,cache) + fib(n-2,cache)
    cache[n] = res
    return res

if __name__ == '__main__':
    n = 100
    re = fib(n,{})
    print(re)