"""
46：全排列
链接：https://leetcode-cn.com/problems/permutations/
难度：中等
标签：dfs
评价：dfs模板，必须掌握！
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, path):
            if not nums:
                ans.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        ans = []
        dfs(nums, [])
        return ans
