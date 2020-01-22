"""
399：除法求值
难度：中等
标签：dfs、图、并查集
评价：中等题目里面较难的题目，用并查集是最好的方法，不过实现起来还是很麻烦。
"""

# dfs解法
class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = {}
        for (x, y) , v in zip(equations, values):
            if x not in graph:
                graph[x] = {}
            graph[x][y] = v
            if y not in graph:
                graph[y] = {}
            graph[y][x] = 1 / v
        
        def dfs(s, t):
            if s not in graph:
                return -1
            if t == s:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, t)
                    if v != -1:
                        return graph[s][node] * v
            return -1

        ans = []
        for qs, qt in queries:
            visited = set()
            ans.append(dfs(qs, qt))
        return ans


# 并查集解法
class Node(object):
    def __init__(self, parent = -1, weight = -1):
        self.parent = parent
        self.weight = weight

class UnionSet(object):
    def __init__(self, n):
        self.parent = [Node(i) for i in range(n)]

    def __str__(self):
        return ",".join([str(i) for i in self.parent])

    def find(self, num):
        root = num
        while root != self.parent[root]:
            root = self.parent[root]
        while num != root:
            self.parent[num], num = root, self.parent[num]
        return root

    def union(self, num1, num2):
        self.parent[self.find(num2)] = self.find(num1)
    
    def count(self):
        return len([1 for i, num in enumerate(self.parent) if i == num])


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        alph = {}
        for equation in equations:
            for i in range(2):
                if equation[i] not in alph:
                    alph[equation[i]] = len(alph)
        unionset = UnionSet(len(alph))
        for equation in equations:
            unionset.union(alph[equation[0]], alph[equation[1]])
        print(unionset)

        ans = []
        for query in queries:
            if query[0] not in alph or query[1] not in alph:
                ans.append(-1)
            else:
                pass
        return ans