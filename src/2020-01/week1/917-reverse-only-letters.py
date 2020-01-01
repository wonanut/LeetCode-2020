"""
917: reverse-only-letters
@Author: wonanut
@Date: 2020-1-1

有两种思路，我优先想到的是双指针，前后指针
另外看到有使用栈实现的，解法也挺巧妙
class Solution:
    def reverseOnlyLetters(self, S):
        p = [i for i in S if i.isalpha()]
        return ''.join([i if not i.isalpha() else p.pop() for i in S])
"""

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        left, right = 0, len(S) - 1
        while left < right:
            if not S[left].isalpha():
                left += 1
            elif not S[right].isalpha():
                right -= 1
            else:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
        return "".join(S)
            