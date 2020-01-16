"""
764：最大加号标志（largest-plus-sign）
难度：中等
标签：动态规划
评价：这道题目只想到了暴力解法，遍历N^2个点分别作为加号标志的中心，
然后分别计算其上下左右连续的1的个数，时间复杂度O(n^3)，肯定是超时了的。
然后我就开始瞎想了，想到了分治，发现也不好实现。最后看了官方题解发现还是
使用动态规划来求解的，思想也是基于暴力算法进行优化的。
"""

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        if len(mines) == 0:
            return N // 2

        ans = 0
        banned = {tuple(mine) for mine in mines}
        dp = [[0 for i in range(N)] for j in range(N)]
        for i in range(0, N):
            # 从左往右，找左边的臂长
            count = 0
            for j in range(0, N):
                count = 0 if (i,j) in banned else count + 1
                dp[i][j] = count
            # 从右往左，找右边的臂长
            count = 0
            for j in range(N - 1, -1, -1):
                count = 0 if (i,j) in banned else count + 1
                dp[i][j] = min(count, dp[i][j])

        for j in range(0, N):
            # 从上往下
            count = 0
            for i in range(0, N):
                count = 0 if (i,j) in banned else count + 1
                dp[i][j] = min(count, dp[i][j])
            # 从下往上
            count = 0
            for i in range(N -1 , -1, -1):
                count = 0 if (i,j) in banned else count + 1
                dp[i][j] = min(count, dp[i][j])
                ans = max(ans, dp[i][j])
        return ans
