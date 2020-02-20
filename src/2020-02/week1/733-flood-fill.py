"""
733：图像渲染
链接：https://leetcode-cn.com/problems/flood-fill/
难度：简单
标签：深度优先搜索
评价：简单的dfs基础问题，但是有一点容易忽略：如果要更改的值和原本的值相同，应该直接返回，否则会陷入死循环
"""

# 递归解法
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(row, col, val):
            image[row][col] = newColor
            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r_, c_ = row + d[0], col + d[1]
                if r_ >= 0 and r_ < len(image) and c_ >= 0 and c_ < len(image[0]) and image[r_][c_] == val:
                    dfs(r_, c_, val)

        if image[sr][sc] == newColor:
            return image
        dfs(sr, sc, image[sr][sc])
        return image


# 非递归解法
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        origin_value = image[sr][sc]
        if origin_value == newColor:
            return image
        stack = []
        stack.append((sr, sc))
        while len(stack) != 0:
            row, col = stack.pop()
            image[row][col] = newColor
            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r_, c_ = row + d[0], col + d[1]
                if r_ >= 0 and r_ < len(image) and c_ >= 0 and c_ < len(image[0]) and image[r_][c_] == origin_value:
                    stack.append((r_, c_))

        return image