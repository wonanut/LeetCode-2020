"""
71：simplify-path
分析：栈的应用
@Author：wonanut
@Date：2019-12-31
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for item in path.split('/'):
            if item == '' or item == '.':
                continue
            elif item == '..':
                if len(stack):
                    stack.pop()
            else:
                stack.append(item)
            
        ans = ''
        while len(stack):
            ans = '/' + stack.pop() + ans
        return ans if len(ans) else "/"