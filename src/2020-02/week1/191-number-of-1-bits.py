"""
191：位1的个数
链接：https://leetcode-cn.com/problems/number-of-1-bits/solution/wei-1de-ge-shu-by-leetcode/
难度：简单
标签：位运算
评价：题目本身很简单，但是可以综合考验对位运算的了解程度。
"""

# 最基础的方法：右移
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            if n & 0x1:
                ans += 1
            n >>= 1
        return ans

# 更好的方法
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n != 0:
            ans += 1
            n = n & (n - 1)
        return ans