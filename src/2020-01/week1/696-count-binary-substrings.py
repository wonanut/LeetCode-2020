"""
696 计数二进制子串
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
重复出现的子串要计算它们出现的次数。

@难度：简单
@知识点：字符串数组，常规
@存在问题：卡壳了，其实此类题目只需认真分析即可，没有太大难度
@Date：2020-1-3
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        prev, cur = 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                ans += min(prev, cur)
                prev = cur
                cur = 1
        ans += min(prev, cur)
        return ans