"""
932：漂亮数组
难度：中等
标签：分治、有点难
评价：这道题的解法是真的很难想到，即使我看了别人的题解，也还没有完全理解为什么他们这样做能够解决这个问题；太难想到了，待整理。
"""

class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        def helper(arr):
            if len(arr) <= 2:
                return arr
            
            left = helper(arr[::2])
            right = helper(arr[1::2])
            return left + right

        return helper([i for i in range(1, N+1)])
