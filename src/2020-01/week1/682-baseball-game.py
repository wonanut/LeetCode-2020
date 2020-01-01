"""
682 棒球比赛
分析：栈的应用，简单题
@Author：wonanut
@Date：2019-12-31
"""

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = 0
        stack = []
        for ch in ops:
            if ch == '+':
                temp1, temp2 = stack[-1], stack[-2]
                stack.append(temp1 + temp2)
                ans += stack[-1]
            elif ch == 'D':
                stack.append(2 * stack[-1])
                ans += stack[-1]
            elif ch == 'C':
                ans -= stack[-1]
                stack.pop()
            else:
                stack.append(int(ch))
                ans += stack[-1]
            
        return ans