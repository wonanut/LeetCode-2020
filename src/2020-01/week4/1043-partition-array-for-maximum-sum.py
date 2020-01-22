"""
1043:分隔数组以得到最大和
难度：中等
标签：动态规划
链接：https://leetcode-cn.com/problems/partition-array-for-maximum-sum/submissions/
评价：属于中等偏难的动态规划题目，不是很容易想到状态转移方程，在参考了题目提示之后写出来一个dp，但是超时了。
下面的解法是参考别人的最优写法:对于数组求 最大  最小问题 一般为 动态规划问题.
申请dp数组：dp = [0 for i in range(len(A) + 1)]
状态转移方程：dp[i] = max{dp[i - j] + max{A[i - t]} * j}, for t in range(1,j + 1), for j in range(1, K + 1)
返回:dp[len(A)]
"""


class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0 for i in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            max_temp = A[i - 1]
            for j in range(1, K + 1):
                if i >= j:
                    max_temp = max(max_temp, A[i - j])
                    dp[i] = max(dp[i], dp[i - j] + max_temp * j)
        return dp[len(A)]