"""
953：验证外星词典
难度：简单
标签：哈希表
评价：没有太好的办法，老实做就好了，这是简单题目的基本套路。
"""

# 方法1：遍历
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_index = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_index[word1[j]] > order_index[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False

        return True

# 方法2：排序，虽然代码就一行但它的效率差啊（狗头）
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        return words == sorted(words, key=lambda w: [order.index(x) for x in w])