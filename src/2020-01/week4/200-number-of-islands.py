"""
200: 岛屿数量
难度：中等
标签：并查集、图、深度优先搜索
评价：如果了解并查集以及DFS之后写这道题没有很大的问题，一开始用并查集的解法反而复杂了。
"""

# DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(m, n, row, col):
            grid[row][col] = '0'
            for i in [-1, 1]:
                if row + i >= 0 and row + i < m and grid[row + i][col] == '1':
                    dfs(m, n, row + i, col)
            for j in [-1, 1]:
                if col + j >= 0 and col + j < n and grid[row][col + j] == '1':
                    dfs(m, n, row, col + j)

        if len(grid) == 0:
            return 0

        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(m, n, i, j)
        return ans

# 并查集
class UnionSet(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, num):
        if num == self.parent[num]:
            return num
        return self.find(self.parent[num])

    def union(self, num1, num2):
        self.parent[self.find(num1)] = self.find(num2)
    
    def count(self):
        ans = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                ans += 1 
        return ans

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(unionset, m, n, row, col):
            grid[row][col] = '0'
            for i in [-1, 1]:
                if row + i >= 0 and row + i < m and grid[row + i][col] == '1':
                    unionset.union(n * row + col, n * (row + i) + col)
                    dfs(unionset, m, n, row + i, col)
            for j in [-1, 1]:
                if col + j >= 0 and col + j < n and grid[row][col + j] == '1':
                    unionset.union(n * row + col, n * row + col + j)
                    dfs(unionset, m, n, row, col + j)

        if len(grid) == 0:
            return 0
            
        m, n = len(grid), len(grid[0])
        zeros = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    zeros += 1
        unionset = UnionSet(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(unionset, m, n, i, j)
        print(unionset.parent)
        return unionset.count() - zeros