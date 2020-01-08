"""
223: rectangle area
难度：中等
题目本身不难，我自己没理清，逻辑混乱
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if A >= G or B >= H or C <= E or D <= F:
            return (H - F) * (G - E) + (C - A) * (D - B)

        a = max(A,E)
        c = min(C,G)
        b = max(B,F)
        d = min(D,H)
        return (C - A) * (D - B) - (c - a) * (d - b) + (G - E) * (H - F)
