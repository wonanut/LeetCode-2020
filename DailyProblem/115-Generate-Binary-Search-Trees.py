"""
Daily Problem 115: Generate-Binary-Search-Trees
题目来源：微信公众号-Daily Problem
https://mp.weixin.qq.com/s/RXQDzpZVjV6ZL31RxtPisg

Given a number n, generate all binary search trees that can be constructed with nodes 1 to n.
"""

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		result = str(self.value)
		if self.left:
			result = result + str(self.left)
		if self.right:
			result = result + str(self.right)
		return result


def helper(low, high):
	if low == high:
		return [None]
	result = []
	for i in range(low, high):
		left = helper(low, i)
		right = helper(i + 1, high)
		for l in left:
			for r in right:
				result.append(Node(i, l, r))
	return result


def generate_bst(n):
	# Fill this in.
	return helper(1, n + 1)


for tree in generate_bst(4):
	print(tree)

# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1
