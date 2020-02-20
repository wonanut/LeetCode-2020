"""
687：最长同值路径
链接：https://leetcode-cn.com/problems/longest-univalue-path/
难度：简单？？？
标签：递归
评价：经典递归问题吧，有点难，但是是标准的递归模板问题
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type head: TreeNode
        :rtype: int
        """
        self.ans = 0

        def helper(head):
            if not head: return 0
            
            left = helper(head.left)
            right = helper(head.right)
            ll, rl = 0, 0
            if head.left and head.val == head.left.val:
                ll = left + 1
            if head.right and head.val == head.right.val:
                rl = right + 1
            self.ans = max(self.ans, ll + rl)
            return max(ll, rl)
        
        helper(root)
        return self.ans