"""
1162：地图分析
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible/
难度：中等
标签：广度优先遍历
评价：典型的广度优先遍历问题，我先使用深度优先遍历实现了一下超时了。
"""

# 以下是使用dfs实现的代码，超时了。
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(row, col, depth):
            if grid[row][col] == 1:
                temp_ans[0] = min(temp_ans[0], depth)
                return

            visited.append([row, col])
            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                row_, col_ = row + d[0], col + d[1]
                if row_ >= 0 and row_ < len(grid) and col_ >= 0 and col_ < len(grid) and [row_, col_] not in visited:
                    dfs(row_, col_, depth + 1)
            visited.pop()

        ans = 0.1
        visited = []
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                temp_ans = [1e5]
                if grid[i][j] == 0:
                    dfs(i, j, 0)
                    ans = max(temp_ans[0], ans)
                counter += grid[i][j]
        
        if counter == 0 or ans == 0.1:
            return -1
        return ans