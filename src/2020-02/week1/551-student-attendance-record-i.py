"""
551：学生出勤记录I
链接：https://leetcode-cn.com/problems/student-attendance-record-i/
难度：简单
标签：python函数，字符串数组
评价：可以组个处理字符串，也可调用python字符串匹配: "LLL" in s
"""

# 我的朴素解法：
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'A': 0, 'L': 0, 'P': 0}
        flag = True
        for index, ch in enumerate(list(s)):
            if index > 1 and ch == s[index - 1] == s[index - 2] == 'L':
                flag = False
            d[ch] += 1
        return d['A'] <= 1 and flag


# python一行代码：python专属
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') <= 1 and not 'LLL' in s