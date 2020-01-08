"""
838：push dominoes
难度：中等
这道题写起来还真的不容易，我自己没想到解法，看到题解后发现主要有两种解法。本题归为难题，需要整理。
"""

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        ans = []
        left = 0
        temp = 'L' + dominoes + 'R'
        for i in range(0, len(temp)):
            if temp[i] in "LR":
                if temp[left] == 'L' and temp[i] == 'R':
                    ans.append('.' * (i - left - 1))
                    ans.append('R')
                elif temp[left] == 'L' and  temp[i] == 'L':
                    ans.append('L' * (i - left))
                elif temp[left] == 'R' and temp[i] == 'R':
                    ans.append('R' * (i - left))
                elif temp[left] == 'R' and temp[i] == 'L':
                    length = i - left - 1
                    half = length // 2
                    if length % 2:
                        ans.append('R' * half + '.' + 'L' * half)
                    else:
                        ans.append('R' * half + 'L' * half)
                    ans.append('L')
                left = i
        return "".join(ans)[:-1]
