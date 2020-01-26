"""
96：不同的二叉搜索树
难度：中等
标签：递归，二叉搜索树
评价：和95题很像
"""

# 使用下面的类似95题的解法会超时，通过12/19个测试用例
class Solution:
    def numTrees(self, n: int) -> int:
        def helper(low, high):
            if low == high:
                return 1
            result = 0
            for i in range(low, high):
                left = helper(low, i)
                right = helper(i + 1, high)
                result += left * right
            return result
        return helper(1, n + 1)


# 使用备忘录的方法
class Solution(object):
    def numTrees(self, n):
        def helper(arr):
            if len(arr) <= 1:
                return 1
            if record[len(arr)] != 0:
                return record[len(arr)]
            
            ans = 0
            for i in range(len(arr)):
                left, right = helper(arr[:i]), helper(arr[i + 1:])
                ans += left * right
            record[len(arr)] = ans
            return ans

        arr = [i for i in range(1, n + 1)]
        record = {i: 0 for i in range(1, n + 1)}
        return helper(arr)

# 动态规划解法
class Solution(object):
    def numTrees(self, n):
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
