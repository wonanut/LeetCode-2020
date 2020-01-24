"""
916: 单词子集
链接：https://leetcode-cn.com/problems/word-subsets/
难度：中等
标签：字符串
评价：中规中矩的字符串题目，没有什么技巧，我还想复杂了。
"""

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        dict_b = [0 for i in range(26)]
        for b in B:
            dict_temp = [0 for i in range(26)]
            for ch in b:
                dict_temp[ord(ch) - ord('a')] += 1
                dict_b[ord(ch) - ord('a')] = max(dict_b[ord(ch) - ord('a')], dict_temp[ord(ch) - ord('a')])

        ans = []
        for a in A:
            dict_a = [0 for i in range(26)]
            for ch in a:
                dict_a[ord(ch) - ord('a')] += 1
            i = 0
            while i < 26:
                if dict_a[i] < dict_b[i]:
                    break
                i += 1
            if i == 26:
                ans.append(a)
        return ans