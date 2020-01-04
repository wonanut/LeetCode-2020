"""
984:string-without-aaa-or-bbb
这是一道很烦的题目，就是逻辑题目，贪心思想，只有一种一种情况分析然后写代码实现。
可以把初始情况分为三种：
1. A > B
2. B > A
3. A = B
最后前两种情况都会转变为第三种情况，否则就会无解。因此直接一个while循环每次更新A和B的值即可。
"""

class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ans = ""
        while A > 0 or B > 0:
            if A == B:
                ans += "ab" * A
                A = 0
                B = 0
            elif A > B:
                if A > 1:
                    ans += 'aa'
                    A -= 2
                elif A == 1:
                    ans += 'a'
                    A -= 1
                if B > 0:
                    ans += 'b'
                    B -= 1
            else:
                if B > 1:
                    ans += 'bb'
                    B -= 2
                elif B == 1:
                    ans += 'b'
                    B -= 1
                if A > 0:
                    ans += 'a'
                    A -= 1
        return ans
                
