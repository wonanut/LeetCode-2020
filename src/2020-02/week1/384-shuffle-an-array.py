"""
384：打乱数组
链接：https://leetcode-cn.com/problems/shuffle-an-array/
难度：中等
标签：洗牌算法、数组、随机
评价：这道题会的不难，不会的做不出来（如果不调用api的话），这题考察的是洗牌算法（以及编写测试用例）
"""

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.back_up = nums[:]
        self.ans = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.ans = self.back_up[:]
        return self.ans

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        right = len(self.ans) - 1
        while right > 0:
            rand = random.randint(0, right)
            self.ans[rand], self.ans[right] = self.ans[right], self.ans[rand]
            right -= 1
        return self.ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()