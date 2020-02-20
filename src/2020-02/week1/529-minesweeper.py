"""
529：扫雷游戏
链接：https://leetcode-cn.com/problems/minesweeper/
难度：中等
标签：深度优先搜索
评价：经典中的经典深度/广度优先搜索题目，大致的思路没有问题，但是我陷入了一个bug之中挣扎了几十分钟(后面发现只需要加一个判断就可以了！)，下面贴出我的犯错误的代码。
"""

# 这是我一开始的错误解法
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def check(row, col):
            counter = 0
            for d in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                r_, c_ = row + d[0], col + d[1]
                if r_ >= 0 and r_ < len(board) and c_ >= 0 and c_ < len(board[0]) and board[r_][c_] == 'M':
                    counter += 1
            return counter

        def dfs(row, col):
            counter = check(row, col)
            board[row][col] = str(counter) if counter != 0 else 'B'
            for d in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                r_, c_ = row + d[0], col + d[1]
                if r_ >= 0 and r_ < len(board) and c_ >= 0 and c_ < len(board[0]) and board[r_][c_] == 'E':
                    dfs(r_, c_)
            
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            dfs(click[0], click[1])

        return board


# dfs解法
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def check(row, col):
            counter = 0
            for d in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                r_, c_ = row + d[0], col + d[1]
                if r_ >= 0 and r_ < len(board) and c_ >= 0 and c_ < len(board[0]) and board[r_][c_] == 'M':
                    counter += 1
            return counter
            

        def dfs(row, col):
            counter = check(row, col)
            board[row][col] = 'B' if counter == 0 else str(counter)
            if counter == 0:
                for d in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    r_, c_ = row + d[0], col + d[1]
                    if r_ >= 0 and r_ < len(board) and c_ >= 0 and c_ < len(board[0]):
                        if board[r_][c_] == 'E':
                            dfs(r_, c_)
            
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            dfs(click[0], click[1])

        return board

