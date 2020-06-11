"""
@auth whs
@time 2020-06-10
@name
@info
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0 or x < 10: return True
        s = str(x)
        n = len(s)
        # for i in range(n):
        #     if s[i] != s[n-i-1]:
        #         return False
        #     if 2*i == n or 2*i + 1> n:
        #         return True
        a = [s[i] for i in range(n)]
        for i in range(n):
            if 2 * i + 1 > n:
                break
            a[i] , a[n-1-i] = a[n-1-i] , a[i]
        if a == [s[i] for i in range(n)]:
            return True
        return False

if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome(10))