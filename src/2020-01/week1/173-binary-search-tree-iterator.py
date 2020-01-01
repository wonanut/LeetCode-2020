"""
173 binary-search-tree-iterator
分析：考察二叉树中序遍历的非递归实现，借助栈实现
@Author：wonanut
@Date：2019-12-31
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        
        cur = self.stack.pop()
        if cur.right:
            node = cur.right
            while node:
                self.stack.append(node)
                node = node.left

        return cur.val
        
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()