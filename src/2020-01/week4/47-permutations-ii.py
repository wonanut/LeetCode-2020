"""
47：全排列ii
难度：中等
标签：回溯
评价：和46题类似，加上去重就好了。问题在于，如何通过避免检查数组是否已经存在？待整理
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, arr):
            if len(nums) == 0:
                if arr not in ans:
                    ans.append(arr)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], arr + [nums[i]])

        ans = []
        dfs(nums, [])
        return ans