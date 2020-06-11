"""
@auth whs
@time 2020-06-10
@name 快速幂算法
@info pow(x,n) x的n次方
"""

def pow(x,n):
    if n == 0:
        return 1
    if n < 0 :
        x = 1/x
        n = -n
    half = pow(x,n//2)
    if n%2==0:
        return half * half
    else:
        return half * half * x


if __name__ == '__main__':
    print(pow(5,-5))