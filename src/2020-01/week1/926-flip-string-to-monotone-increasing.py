"""
926:flip-string-to-monotone-increasing
这道题很有意思，是考验逻辑思维能力的一道题，我没想出来这个解法
@Author: wonanut
@Date: 2020-1-1
"""

class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        # zero_count 统计分界点之后的0的个数（即讲分界点之后的0全部变为1所需要的代价），初始时分界点在最左边
        zero_count = S.count('0')
        counter = [zero_count]
        for i in range(len(S)):
            # 如果是1，则需要将其改为0，代价+1
            if S[i] == '1':
                zero_count += 1
            # 如果是0，则当前值不需要修改，分界点之后的0的个数减少1
            else:
                zero_count -= 1
            counter.append(zero_count)
        return min(counter)
        