"""
77：组合
链接：https://leetcode-cn.com/problems/combinations/
难度：中等
标签：回溯
评价：使用dfs模板很好实现，而且相比于排列问题更简单，但是我写的代码不是最好的，需要改进优化。
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(nums, arr):
            if len(arr) == k:
                ans.append(arr)
                return
            if len(nums) == 0:
                return

            for i in range(len(nums)):
                helper(nums[i + 1:], arr + [nums[i]])

        ans = []
        helper([i for i in range(1, n + 1)], [])
        return ans