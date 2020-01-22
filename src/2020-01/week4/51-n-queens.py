"""
51：n皇后问题
难度：困难
标签：回溯
评价：这是一道经典难题，难在简洁且高效的写出来。下面的代码是我自己写的，感觉很精炼了！
"""

class Solution(object):
    def solveNQueens(self, n):
        def helper(row, flag_col, flag_a, flag_b):
            """
            对于二维数组中的点(i, j)，位于主对角线上的点j-i相同，位于副对角线上的i+j相同
            flag_col 中存储列
            flag_a 中存储正对角线之差
            flag_b 中存储副对角线之和
            """
            if row == n:
                ans.append(["".join(m[i]) for i in range(n)])
                return
            for i in range(n):
                if i not in flag_col and i - row not in flag_a and i + row not in flag_b:
                    m[row][i] = 'Q'
                    flag_col.append(i)
                    flag_a.append(i - row)
                    flag_b.append(i + row)
                    helper(row + 1, flag_col, flag_a, flag_b)
                    flag_col.pop()
                    flag_a.pop()
                    flag_b.pop()
                    m[row][i] = '.'

        ans = []
        m = [['.' for i in range(n)] for j in range(n)]
        helper(0, [], [], [])
        return ans