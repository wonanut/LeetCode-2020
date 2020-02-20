"""
752：打开转盘锁
链接：https://leetcode-cn.com/problems/open-the-lock/
难度：中等
标签：BFS
评价：很容易的就想到了应该使用BFS，然而代码提交一直超时。后来发现只要将deadends转化为set就好了。因为set的查找时间复杂度为O(1)！
"""

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)

        queue = [("0000", 0)]
        visited = {"0000"}
        while len(queue) != 0:
            cur = queue.pop(0)
            if cur[0] in deadends:
                continue
            if cur[0] == target:
                return cur[1]
            for i in range(4):
                temp = cur[0][:i] + str((int(cur[0][i]) + 1) % 10) + cur[0][i + 1:]
                if temp not in deadends and temp not in visited:
                    visited.add(temp)
                    queue.append((temp, cur[1] + 1))
                temp = cur[0][:i] + str((int(cur[0][i]) + 9) % 10) + cur[0][i + 1:]
                if temp not in deadends and temp not in visited:
                    visited.add(temp)
                    queue.append((temp, cur[1] + 1))
        return -1