class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        stack = []
        for ch in preorder.split(','):
            stack.append(ch)
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                if stack[-1] == '#':
                    return False
                stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack[0] == '#'