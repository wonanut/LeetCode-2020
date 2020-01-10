"""
1029：两地调度
难度；简单
标签：贪心
"""

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        ans = 0
        costs.sort(key = lambda x: x[0] - x[1])
        for i in range(len(costs)):
            ans += costs[i][0] if i < len(costs) / 2 else costs[i][1]
        return ans        