"""
946: 验证栈序列
难度：中等
标签：栈
评价：题目不是太难，但我感觉我的这个模拟的思路比较笨。
"""

# 我的做法
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0:
            return True
        stack = []
        stack.append(pushed.pop(0))
        while len(pushed) != 0:
            if len(stack) == 0 and len(pushed) == 0 and len(popped) == 0:
                return True
            if len(stack) != 0 and len(pushed) == 0 and len(popped) != 0:
                return False

            if len(stack) > 0 and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
            elif len(pushed) > 0:
                stack.append(pushed.pop(0))

        return stack[::-1] == popped


# 更好的模拟方法
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while len(stack) > 0 and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        return len(stack) == 0