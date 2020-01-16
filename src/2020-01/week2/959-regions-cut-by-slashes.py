"""
959 regions-cut-by-slashes
难度：中等
标签：深度优先搜搜，并查集
评价：不会，参考的题解才写出来的，两种解法：dfs或者并查集。
"""

## 深度优先遍历解法，将一个小正方形转变为3*3的小矩阵，最终生成一个3n*3n的矩阵，做dfs
## 题解：https://leetcode-cn.com/problems/regions-cut-by-slashes/solution/mei-ge-xiao-ge-fen-jie-wei-3-3-fang-ge-qiu-lian-to/
class Solution(object):
    def __init__(self):
        self.ans = 0
        self.mat = None

    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= len(self.mat) or j >= len(self.mat):
            return

        if self.mat[i][j] == 0:
            self.mat[i][j] = 1
            self.dfs(i, j + 1)
            self.dfs(i, j - 1)
            self.dfs(i - 1, j)
            self.dfs(i + 1, j)

    def regionsBySlashes(self, grid):
        """
        dfs
        """
        n = len(grid)
        self.mat = [[0 for i in range(n * 3)] for j in range(n * 3)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    self.mat[i*3 + 0][j*3 + 2] = 1
                    self.mat[i*3 + 1][j*3 + 1] = 1
                    self.mat[i*3 + 2][j*3 + 0] = 1
                elif grid[i][j] == ' ':
                    continue
                else:
                    self.mat[i*3 + 0][j*3 + 0] = 1
                    self.mat[i*3 + 1][j*3 + 1] = 1
                    self.mat[i*3 + 2][j*3 + 2] = 1

        for i in range(3 * n):
            for j in range(3 * n):
                if self.mat[i][j] == 0:
                    self.ans += 1
                    self.dfs(i, j)

        return self.ans

                
## 并查集解法⭐⭐⭐⭐⭐
class UnionSet(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, num):
        if self.parent[num] == num:
            return self.parent[num]
        return self.find(self.parent[num])
    
    def union(self, num1, num2):
        self.parent[self.find(num1)] = self.find(num2)

    def count(self):
        return len([1 for i, num in enumerate(self.parent) if num == i])

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        unionset = UnionSet(4 * n * n)
        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                if grid[i][j] == '/':
                    unionset.union(root + 0, root + 3)
                    unionset.union(root + 1, root + 2)
                if grid[i][j] == '\\':
                    unionset.union(root + 0, root + 1)
                    unionset.union(root + 2, root + 3)
                if grid[i][j] == ' ':
                    unionset.union(root + 0, root + 1)
                    unionset.union(root + 1, root + 2)
                    unionset.union(root + 2, root + 3)
                    
                if i > 0:
                    unionset.union(root + 0, root - 4 * n + 2)
                if j > 0:
                    unionset.union(root + 3, root - 3)
        
        return unionset.count()