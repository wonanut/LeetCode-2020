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
            # If reached the end of a branch, return False.
            if not root:
                return False

            # Left and Right Recursion
            left = helper(root.left)
            right = helper(root.right)

            # If the current node is one of p or q
            mid = p == root or q == root

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                ans[0] = root
            
            # Return True if either of the three bool values is True.
            return mid or left or right
        
        ans = [None]
        helper(root)
        return ans[0]

    # 另一种方法太牛皮
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Return root if left or right is False, otherwise left or right
        return root if (left and right) else (left or right)