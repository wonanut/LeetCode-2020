"""
463：岛屿的周长
链接：https://leetcode-cn.com/problems/island-perimeter/
难度：简单
标签：矩阵、逻辑
评价：这道题一开始我想的是深度优先遍历，能够轻松计算到岛屿面积（肯定比两层遍历效率高），但是求周长还是有点麻烦。
后面参考别人的思路，直接遍历一遍就行了，岛屿四周为0的个数之和就是周长！
不过这个方法的效率很低，还有效率更高的：直接检查方块1的左边和上边的方块1的个数，即为邻居墙壁的个数
"""


# 方法1
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        i_, j_ = i + d[0], j + d[1]
                        if i_ >= 0 and i_ < len(grid) and j_ >= 0 and j_ < len(grid[0]):
                            if grid[i_][j_] == 0:
                                ans += 1
                        else:
                            ans += 1
        return ans


# 方法2：
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        H, W = len(grid), len(grid[0])
        area = 0
        connect = 0
        for r in range(H):
            for c in range(W):
                if grid[r][c] == 1:
                    area += 1
                    # check up and left
                    if r > 0 and grid[ r -1][c] == 1: connect += 1
                    if c > 0 and grid[r][ c -1] == 1: connect += 1
        return area * 4 - 2 * connect