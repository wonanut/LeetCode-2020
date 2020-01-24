"""
93:复原IP地址
链接：https://leetcode-cn.com/problems/restore-ip-addresses/
难度：中等
标签：字符串、回溯
评价：中规中矩的dfs问题，算比较简单的了，我直接就写出来了。
不足：由于使用的int()强制将字符串转换成整数，没有考虑到第一位为0且长度大于1的字符串的情况，因此WA了一次。
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def helper(s, arr):
            if len(arr) == 4:
                if len(s) == 0:
                    ans.append(".".join(arr))
                return
            for i in range(1, 4):
                if len(s) >= i and int(s[:i]) < 256 and int(s[:i]) >= 0:
                    if s[0] == '0' and i > 1:
                        continue
                    arr.append(s[:i])
                    helper(s[i:], arr)
                    arr.pop()

        ans = []
        helper(s, [])
        return ans