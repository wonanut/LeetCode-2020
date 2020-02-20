"""
201：数字范围按位与
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/
难度：中等
标签：位运算
评价：作为一个中等题肯定不能暴力通过，需要仔细分析！
总结的比较好的：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--41/
"""

# 暴力解法
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = m
        while m <= n:
            ans &= m
            m += 1
        return ans

# 优化
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = 0xFFFFFFFF
        basic = 1
        while m != 0 and m & 0x1 == 0:
            basic = basic << 1
            m = m >> 1
            n = n >> 1
        stop = m * 2
        while m <= n and m <= stop:
            ans &= m
            m += 1
        return ans * basic

# 高手答案
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i