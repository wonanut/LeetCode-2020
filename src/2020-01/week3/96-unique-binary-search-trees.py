"""
96：不同的二叉搜索树
难度：中等
标签：递归，二叉搜索树
评价：和95题很像
"""

# 使用下面的类似95题的解法会超时，通过12/19个测试用例
class Solution:
    def numTrees(self, n: int) -> int:
        def helper(low, high):
            if low == high:
                return 1
            result = 0
            for i in range(low, high):
                left = helper(low, i)
                right = helper(i + 1, high)
                result += left * right
            return result
        return helper(1, n + 1)


