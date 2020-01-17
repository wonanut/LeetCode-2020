"""
342: 4的幂次方
难度：简单
标签：位运算
评价：4的幂次方1，4，16，64，...,其二进制的特点是只有一位为1且1只能在奇数位。如何不使用循环或者递归完成这道题目呢？
"""

# 方法1：列举4^0, 4^1, 4^2,...,4^15
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        target = [1] * 16
        for i in range(1, 16):
            target[i] = target [i - 1] * 4
        return num in target
        

# 方法2：如果num是4的幂，则有log4(num)=a => 1/2log2(num) = a => log2(num)=2a为偶数
from math import log2 
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log2(num) % 2 == 0

# 方法3：确保num是2的幂，再判断其是2的奇次幂还是偶次幂（4的幂是2的偶次幂）
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 == num
        # 或者
        # return num > 0 and num & (num - 1) = 0 and num & 0xaaaaaaaa == 0

# 方法4：循环
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num > 1:
            if num % 4 != 0:
                return False
            num /= 4
        return num == 1
