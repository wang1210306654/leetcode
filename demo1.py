"""
@auth whs
@time 2020-06-09
@name 三数之和
@info 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。
解析：
1、先从小到大排序
2、从左侧开始，选定第一个数为定值，然后左右指针分别指向定值后一位和最后一位
3、定义的左右和定值相加
    如果等于0，记录下三个值
    如果小于0，左指针右移动
    如果大于0，右指针左移
4、重新选取定值
"""
def demo(nums):
    nums.sort()
    print(nums)
    n = len(nums)  # 获取列表长度
    res = []  # 存放结果

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        num1 = nums[i]  # 取得定值
        if num1 > 0:
            break
        # 定义双指针初始状态
        j = i + 1
        k = n - 1
        while j < k:
            total = num1 + nums[j] + nums[k]
            if total == 0:
                res.append((num1, nums[j], nums[k]))
                j += 1
                k -= 1
                while nums[j] == nums[j - 1] and j < k:j += 1
                while nums[k] == nums[k + 1] and j < k:k -= 1
            elif total > 0:
                k -= 1
                while nums[k] == nums[k + 1] and j < k:k -= 1
            else:
                j += 1
                while nums[j] == nums[j - 1] and j < k:j += 1
    return res

if __name__ == '__main__':
    nums = [1,-1,-1,2,0,0,0,0,-3,-4,7,-3,-1,-4,-5,-7,-5,3,6,9]
    re = demo(nums)
    print(re)

