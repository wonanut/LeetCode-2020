"""
Leetcode 543: 二叉树的直径
简单题，分析：求二叉树的高度的变种
@Author：wonanut
@Date：2019-12-31
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def helper(self, root):
        if not root:
            return 0
        
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.ans = max(self.ans, l + r + 1)
        return max(l, r) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root)
        return self.ans - 1