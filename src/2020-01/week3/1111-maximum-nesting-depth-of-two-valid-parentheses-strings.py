"""
1111：有效括号的嵌套深度
难度：中等
标签：贪心
评价：这道题需要仔细思考，切忌心急。
一开始我也没有想到应该怎么解，后来看了一眼标签写着贪心，就照着贪心的思想自己模拟了一下，就直接写出来了。
"""

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        count1, count2 = 0, 0
        ans = []
        for s in seq:
            if s == '(':
                if count1 <= count2:
                    count1 += 1
                    ans.append(0)
                else:
                    count2 += 1
                    ans.append(1)
            else:
                if count1 <= count2:
                    count2 -= 1
                    ans.append(1)
                else:
                    count1 -= 1
                    ans.append(0)

        return ans