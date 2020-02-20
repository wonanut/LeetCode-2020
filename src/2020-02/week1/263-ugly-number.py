"""
263：丑数
链接：https://leetcode-cn.com/problems/ugly-number/
难度：简单
标签：数学
评价：想复杂了,想成使用bfs求出所有可能解，能AC但是太慢了。其实就是一个数学题：uglyNumber = 1*2^x*3^y*5^z
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1