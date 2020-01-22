"""
409: 最长回文串
难度：简单
标签：哈希表
评价：简单题，但仍有优化代码的余地，代码太长而且耗时较长
"""

# 我的代码
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter_dict = {}
        for ch in s:
            if ch not in counter_dict:
                counter_dict[ch] = 0
            counter_dict[ch] += 1
        ans, flag = 0, False
        for counter in counter_dict:
            if counter_dict[counter] & 0x1 == 0:
                ans += counter_dict[counter]
            else:
                flag = True
                if counter_dict[counter] > 1:
                    ans += counter_dict[counter]
                    ans -= 1
        if flag:
            ans += 1
        return ans

# 优秀代码
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(set(s))
        odd, flag = 0, 0
        for ch in l:
            counter = s.count(ch)
            if counter % 2 == 1:
                flag = 1
                odd += 1
        return len(s) - odd + flag

# 最短的代码
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s) - max(0, sum([s.count(i)%2 for i in set(s)]) - 1)