"""
@auth whs
@time 2020-06-09
@name 字符串反转
@info 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
"""

def reverseString(s,i,n):
    s[n-i] ,s[i] = s[i] ,s[n-i]
    if i < n-i:
        reverseString(s,i+1,n)
    return s

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n ,i = len(s) -1 , 0
        def reverseStrings(s,i,n):
            s[n-i] ,s[i] = s[i] ,s[n-i]
            if i+1 < n-i-1:
                reverseStrings(s,i+1,n)
            return s
        s = reverseStrings(s,i,n)
        return s


if __name__ == '__main__':
    s = ["h","e","l","s"]
    # i ,n = 0, len(s)-1
    # re = reverseString(s,i,n)
    # print(re)
    a = Solution()
    print(a.reverseString(s))