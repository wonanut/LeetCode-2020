"""
Daily Problem 114: Number of Cousins
题目来源：微信公众号-Daily Problem
https://mp.weixin.qq.com/s/_0lmDK_hSMybWPysAsouLA

Given a binary tree and a given node value, return all of the node's cousins. 
Two nodes are considered cousins if they are on the same level of the tree with different parents. 
You can assume that all nodes will have their own unique value.
"""

class Node(object):
	def __init__(self, value, left=None, right=None):
	    self.value = value
	    self.left = left
	    self.right = right

class Solution(object):
	def __find_node(self, tree, val, parent_val, height):
		if tree == None:
			return False
		if tree.value == val:
			return (height, parent_val)
		return (self.__find_node(tree.left, val, tree.value, height + 1) or self.__find_node(tree.right, val, tree.value, height + 1))

	def __get_cousins(self, tree, val, parent, height):
		if tree == None or tree.value == parent:
			return []
		if height == 0:
			return [tree.value]
		return (self.__get_cousins(tree.left, val, parent, height - 1) + self.__get_cousins(tree.right, val, parent, height - 1))

	def list_cousins(self, tree, val):
		height, parent = self.__find_node(tree, val, None, 0)
		return self.__get_cousins(tree, val, parent, height)


#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution().list_cousins(root, 5))
# [4, 6]