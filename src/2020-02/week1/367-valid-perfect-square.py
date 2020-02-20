"""
367：有效的完全平方数
链接：https://leetcode-cn.com/problems/valid-perfect-square/
难度：简单
标签：数学、二分
评价：我第一时间想到的是下面的解法一，后来看到提示可以使用二分查找优化。
"""

# 解法一
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        elif num == 0:
            return True
        sqrt = 1
        cur = sqrt * sqrt
        while cur <= num:
            if cur == num:
                return True
            sqrt += 1
            cur = sqrt * sqrt
        return False

# 解法二： 二分
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False

        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            cur = mid * mid
            if cur == num:
                return True
            if cur < num:
                left = mid + 1
            else:
                right = mid - 1
        return False