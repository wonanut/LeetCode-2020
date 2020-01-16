"""
13:罗马数字转整数
难度：简单
标签：数学，字符串
评价：还算简单，理清楚思路就很容易，把几种特殊情况["IV", 'IX', 'XL', 'XC', 'CD', 'CM']考虑一下就行
比较神奇的是，第一次使用递归写法，第二次优化为迭代，用时反而更多了，搞不懂嗷；下面贴出两种解法。
"""

## 迭代，从左到右遍历字符串
class Solution(object):
    def romanToInt(self, s):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        index, ans = 0, 0
        while index < len(s):
            if index + 1 < len(s) and s[index:index+2] in ["IV", 'IX', 'XL', 'XC', 'CD', 'CM']:
                ans += d[s[index + 1]]
                ans -= d[s[index]]
                index += 2
            else:
                ans += d[s[index]]
                index += 1
        return ans


## 递归
class Solution(object):
    def __init__(self):
        self.d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    def romanToInt(self, s):
        if len(s) == 0:
            return 0

        index = 0
        if len(s) > 1 and (s[0] == 'I' and s[1] in 'VX' or s[0] == 'X' and s[1] in 'LC' or s[0] == 'C' and s[1] in 'DM'):
            return self.d[s[1]] - self.d[s[0]] + self.romanToInt(s[2:])
        else:
            return self.d[s[0]] + self.romanToInt(s[1:])
