"""
1048：最长字符串链
链接：https://leetcode-cn.com/problems/longest-string-chain/
难度：中等
标签：哈希、动态规划
评价：我的思路是对的：先排序然后定义一维dp数组做动态规划，但是写的太复杂，可以优化。
"""

# 我的垃圾代码
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def check(cur, prev):
            for i in range(len(cur)):
            	if cur[:i] + cur[i + 1:] == prev:
            		return True
            return False

        words.sort(key = lambda x: len(x))
        dp = [1 for i in range(len(words) + 1)]
        for i in range(1, len(words) + 1):
            cur_ptr = i - 1
            while cur_ptr >= 1:
                if len(words[i - 1]) - len(words[cur_ptr - 1]) > 1:
                    break
                elif len(words[cur_ptr - 1]) == len(words[i - 1]):
                    cur_ptr -= 1
                    continue
                if check(words[i - 1], words[cur_ptr - 1]):
                    dp[i] = max(dp[i], dp[cur_ptr] + 1)
                cur_ptr -= 1
        return max(dp)


# 优秀代码1
class Solution:
    def longestStrChain(self, words):
        words.sort(key=len)
        note={}
        maxChain=1
        for word in words:
            if word not in note:
                note[word]=1
            for i in range(0,len(word)):
                newWord=word[:i]+word[i+1:]
                if (newWord) in note:
                    note[word]=max(note[word],note[newWord]+1)
            maxChain=max(maxChain,note[word])
        return maxChain


# 优秀代码2
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())