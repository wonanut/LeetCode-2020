"""
113:路径总和II
难度：中等
标签：dfs、二叉树
评价：较为简单，基础的二叉树题目。下面给出两种解法，思路是一样的，第一个是我写的。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
        self.cur = []

    def pathSum(self, root, sum):
        if not root:
            return self.ans
        if not root.left and not root.right:
            if sum == root.val:
                self.cur.append(root.val)
                self.ans.append(self.cur[:])
                self.cur.pop()
        
        self.cur.append(root.val)
        self.pathSum(root.left, sum - root.val)
        self.pathSum(root.right, sum - root.val)
        self.cur.pop()
        return self.ans



## 写法2
class Solution(object):
    def pathSum(self, root, sum):
        def dfs(temp, root, sum):
            if not root:
                return 
            if not root.left and not root.right and sum == root.val:
                temp += [root.val]
                ans.append(temp)
            dfs(temp + [root.val], root.left, sum - root.val)
            dfs(temp + [root.val], root.right, sum - root.val)
        ans = []
        dfs([], root, sum)
        return ans