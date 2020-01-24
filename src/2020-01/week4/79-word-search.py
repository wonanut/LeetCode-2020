"""
79：单词搜索
链接：https://leetcode-cn.com/problems/word-search/submissions/
难度：中等
标签：DFS
评价：经典的回溯问题，标准的DFS模板，待整理。
"""

class Solution(object):
    def exist(self, board, word):
        def dfs(visited, word, row, col):
            if len(word) == 0:
                return True
            
            visited[row][col] = 1
            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                row_, col_ = row + d[0], col + d[1]
                if row_ >= 0 and row_ < len(board) and col_ >= 0 and col_ < len(board[0]) and board[row_][col_] == word[0]:
                    if visited[row_][col_] == 1:
                        continue
                    if dfs(visited, word[1:], row_, col_):
                        return True
            visited[row][col] = 0
            return False

        visited = [[0 for m in range(len(board[0]))] for n in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(visited, word[1:], i, j):
                        return True
        return False