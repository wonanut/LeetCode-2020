"""
95：不同的二叉搜索树2
难度：中等
标签：递归，二叉搜索树
评价：属于较难的递归题目了，好好学习。这道题和DailyProblem115是同一题。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(low, high):
            if low == high:
                return [None]
            result = []
            for i in range(low, high):
                left = helper(low, i)
                right = helper(i + 1, high)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        result.append(node)
            return result
        
        if n == 0:
            return []
        return helper(1, n + 1)