"""
236：二叉树的最近公共祖先
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
难度：中等
标签：二叉树、递归
评价：经典二叉树递归题目，我没写出来，待整理。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def helper(root):
            if not root:
                return False

            left = helper(root.left)
            right = helper(root.right)
            mid = p == root or q == root

            if mid + left + right >= 2:
                ans[0] = root
            
            return mid or left or right
        
        ans = [None]
        helper(root)
        return ans[0]