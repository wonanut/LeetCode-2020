"""
334：递增的三元子序列
难度：中等
标签：贪心
这道题在O（n）的时间复杂度写出来还是有点难度的，这个贪心的思想不太容易理解，有点难度的。
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        first, second = 10e9, 10e9
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
            
        return False