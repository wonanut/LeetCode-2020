"""
1219：黄金矿工
链接：https://leetcode-cn.com/problems/path-with-maximum-gold/
难度：中等
标签：回溯
评价：暴力回溯就完事了，不过效率有点差。
"""

class Solution(object):
    def getMaximumGold(self, grid):
        def helper(row, col, money, path):
            temp = grid[row][col]
            ans[0] = max(ans[0], money + temp)
            grid[row][col] = 0
            for d in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                if d[1] + row >= 0 and d[1] + row < len(grid) and d[0] + col >= 0 and d[0] + col < len(grid[0]) and grid[row + d[1]][col + d[0]] != 0:
                    helper(row + d[1], col + d[0], money + temp, path + [temp])
            grid[row][col] = temp

        ans = [0]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    helper(i, j, 0, [])
        return ans[0]