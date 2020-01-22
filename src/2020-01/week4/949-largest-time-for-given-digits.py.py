"""
949:给定数字能组成的最大时间
难度：简单
标签：数学
评价：这道题真的恶心，最好的办法就是遍历所有的可能然后一个一个判断。我太菜了，写了半个小时都没写出来：）
"""

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        max_t, ans = -1, ""
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2
            sums = hours * 60 + minutes
            if hours < 24 and minutes < 60 and sums > max_t:
                max_t, ans = sums, "{}{}:{}{}".format(h1, h2, m1, m2)
        return "" if max_t == -1 else ans


