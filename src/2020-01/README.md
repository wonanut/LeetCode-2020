## 2020年一月LeetCode解题笔记

Howard Wonanut 2020刷题 / 过于简单的题目不做记录

##### 😃简单题     🤢只会暴力    😡毫无头绪    ⭐题目难度量化    🆕当前周     🕑待整理       ✅已整理      🆘未解决



### week4 1/24 🆕 

- [236-lowest-common-ancestor-of-a-binary-tree](./week4/236-lowest-common-ancestor-of-a-binary-tree.py) `中等` `二叉树经典题目`  ⭐⭐⭐⭐ 🕑



### week4 1/23 🆕 

> 💬 python字母与ascii码相互转换函数：ord('a')，chr(101)

- [47-permutations-ii](./week4/47-permutations-ii.py) `中等` `递归`  ⭐⭐⭐⭐ 🕑
- [916-word-subsets](./week4/916-word-subsets.py) `中等` `字符串`  ⭐⭐⭐
- [52-n-queens-ii](./week4/52-n-queens-ii.py) `困难` `递归经典题目`  ⭐⭐⭐⭐⭐ 🕑
- [77-combinations](./week4/77-combinations.py) `中等` `回溯`  ⭐⭐⭐ 🕑
- [93-restore-ip-addresses](./week4/93-restore-ip-addresses.py) `中等` `回溯`  ⭐⭐⭐
- [1219-path-with-maximum-gold](./week4/1219-path-with-maximum-gold.py) `中等` `回溯`  ⭐⭐⭐⭐



### week4 1/22 🆕 

> 💬949是一道简单题，但是我不会做！！

- [949-largest-time-for-given-digits](./week4/949-largest-time-for-given-digits.py)  `简单` `数学` ⭐⭐⭐⭐⭐⭐⭐ 😡
- [617-merge-two-binary-trees](./week4/617-merge-two-binary-trees.py) `简单` `递归` ⭐⭐
- [200-number-of-islands](./week4/200-number-of-islands.py) `中等` `图` `并查集` `DFS` ⭐⭐⭐
- [46-permutations](./week4/46-permutations.py) `中等` `回溯`  ⭐⭐
- [79-word-search](./week4/79-word-search.py) `中等` `回溯`  ⭐⭐⭐⭐ 🕑

> 💬 python中的二维数组的拷贝需要深拷贝：
>
> import copy
>
> b = copy.deepcopy(a)

- [51-n-queens](./week4/51-n-queens.py) `困难` `递归经典题目`  ⭐⭐⭐⭐⭐



python中itertools库中的combinations和permutations函数可生成组合和排列

```python
import itertools

print(list(itertools.combinations([1,2,3], 2)))
# 输出 [(1, 2), (1, 3), (2, 3)]

print(list(itertools.permutations([1,2,3])))
# 输出 [(1, 2), (1, 3), (2, 3)]
```

使用dfs生成全排列：

```python
# dfs模板，简洁版
def permute(nums):
    def dfs(nums, path):
        if not nums:
            ans.append(path)
            return
        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
    ans = []
    dfs(nums, [])
    return ans


# dfs模板：丑陋版
def permutations(A):
    ans = []
    def dfs(arr):
        if len(arr) == len(A):
            ans.append(arr[:])
            return
        
        for i in range(len(A)):
            if A[i] != -1:
                temp, A[i] = A[i], -1
                arr.append(temp)
                dfs(arr)
                arr.pop()
                A[i] = temp
    dfs([])
    return ans

print(permutations([1,2,3]))
```



### week4 1/21 🆕 

- [1043-partition-array-for-maximum-sum](./week4/1043-partition-array-for-maximum-sum.py)  `中等` `DP` ⭐⭐⭐⭐  😡 🕑



### week3 1/19 🆕 

- [409-longest-palindrome](./week4/409-longest-palindrome.py)  `中等` `哈希` ⭐ 



### week3 1/18 🕑

- [399-evaluate-division](./week3/399-evaluate-division.py)  `中等` `并查集` `图`  ⭐⭐⭐⭐ 🕑



### week3 1/17 🕑

> 💬**卡塔兰数**是组合数学中一个常在各种计算问题中出现的数列，卡塔兰数的一般公式为 C(2n,n)/(n+1)，96题用到了，还有其他问题如**出栈次序问题**也涉及到卡特兰数的应用。

- [95-unique-binary-search-trees-ii](./week3/95-unique-binary-search-trees-ii.py)  `中等` `二叉搜索树`  ⭐⭐⭐ 🕑
- [96-unique-binary-search-trees](./week3/96-unique-binary-search-trees.py)  `中等` `二叉搜索树`  ⭐⭐⭐ 🕑
- [946-validate-stack-sequences](./week3/946-validate-stack-sequences.py)  `中等` `栈`  ⭐⭐

- [342 power-of-four](./week3/342-power-of-four.py)  `简单` `位运算`  ⭐⭐⭐ 🕑

检查一个数是否为2的幂

```python
x > 0 and x & (x - 1) == 0
```



卡塔兰数的递推公式:
$$
G(n)=\sum_{i=1}^n{G(i-1)·G(n-i)}
$$
卡塔兰数便于计算的定义如下：
$$
C_0=1,\quad C_{n}=\frac{1}{n+1}C \left( \begin{array}{1}2n \\ n \end{array} \right)=\frac{(2n)!}{(n+1)!n!}
$$




### week3 1/16 🕑

- [707 design-linked-list](./week3/707-design-linked-list.py)  `中等` `链表`  ⭐ 😃
- [953 verifying-an-alien-dictionary](./week3/953-verifying-an-alien-dictionary.py)  `简单` `哈希`  ⭐⭐⭐ 😡
- [113 path-sum-ii](./week3/113-path-sum-ii.py)  `中等` `dfs`  ⭐⭐ 😃



### week3 1/15 

- [1111 maximum-nesting-depth-of-two-valid-parentheses-strings](./week3/1111-maximum-nesting-depth-of-two-valid-parentheses-strings.py)  `中等` `贪心`  ⭐⭐
- [13 roman-to-integer](./week3/13-roman-to-integer.py)  `简单` `数学` `字符串`  ⭐⭐



### week3 1/14 🕑

> 💬 215，373, 378, 719, 786 都是一些类似的题，都是二分查找的思路。

- [668 kth-smallest-number-in-multiplication-table](./week3/668-kth-smallest-number-in-multiplication-table.py)  `困难` `二分查找`  ⭐⭐⭐⭐⭐ 😡 🆘



### week2 1/13 🕑

> 💬 959可以使用并查集的思想，需要专门整理一下。

- [764 largest-plus-sign](./week2/764-largest-plus-sign.py)  `中等` `动态规划`  ⭐⭐⭐⭐ 🕑
- [959 regions-cut-by-slashes](./week2/959-regions-cut-by-slashes.py)  `中等` `深度优先搜索` `并查集` `图`  ⭐⭐⭐⭐⭐ 🕑

并查集核心代码：

```python
class UnionSet(object):
    def __init__(self, n, init_list = None):
        if init_list:
            self.parent = init_list
        else:
            self.parent = [i for i in range(n)]
    
    def __str__(self):
        return str(self.parent)
    
    # 不带路径压缩的find函数
    def find(self, num):
        if self.parent[num] == num:
            return self.parent[num]
        return self.find(self.parent[num])
       
    # 带路径压缩的find函数:在执行find函数的时候完成路径压缩
    def find(self, num):
        root = num
        while root != self.parent[root]:
            root = self.parent[root]
        while num != root:
            self.parent[num], num = root, self.parent[num]
        return root
    
    def union(self, num1, num2):
        self.parent[self.find(num1)] = self.find(num2)

    def count(self):
        return len([1 for i, num in enumerate(self.parent) if num == i])
```



### week2 1/11 🕑

> 💬 python除法想得到浮点型结果，和C++类似，需要将分子或者分母强制转换为浮点型。否则得到的结果是一个整数。

- [1093 statistics-from-a-large-sample](./week2/1093-statistics-from-a-large-sample.py)  `中等` `数学`  ⭐⭐⭐ 🕑



### week2 1/10 🕑

- [334 increasing-triplet-subsequences](./week2/334-increasing-triplet-subsequence.py)  `中等` `贪心`  ⭐⭐⭐ 🤢 🕑



### week2 1/9 

- [1029 two-city-scheduling](./week2/1029-two-city-scheduling.py)  `简单` `贪心`  ⭐⭐ 🤢



### week2 1/8 

- [933 number-of-recent-calls](./week2/933-number-of-recent-calls.py)  `简单`  ⭐ 😃



### week2 1/6 🕑

- [1162 as-far-from-land-as-possible](./week2/1162-as-far-from-land-as-possible.py)  `中等`  ⭐⭐  🤢  🆘



### week1 1/5 🕑

> 💬 有时候并不一定要使用DP、分治、递归这几类算法思想才能解决问题。很多实际问题的解法需要自己总结观察，将大问题切分为小问题解决，而且解法可能很简单，只是过程很繁琐，需要考虑很多细节问题，如838题。

- [838 push-dominoes](./week1/838-push-dominoes.py)  `中等`  ⭐⭐⭐⭐⭐  😡 🕑



### week1 1/4 🕑

> 💬 有些题目无法使用递归、DP、DFS、分治这些思想实现，只能按照逻辑直接写，如984贪心思想的解法。

- [984 string-without-aaa-or-bbb](./week1/984-string-without-aaa-or-bbb.py)  `中等` `字符串` `贪心` ⭐⭐  🤢 🕑



### week1 1/3 🕑

> 💬 发现遇到字符串数组类题目往往就卡壳了，其实此类题目并没有太多技巧，696题同1/1的926题类似，需要总结。

- [696 count-binary-substrings](./week1/696-count-binary-substrings.py)  `简单` `字符串` ⭐⭐  🤢 



### week1 1/2 🕑

- [934 shortest-bridge]()  `中等` `DFS` `BFS`  😡 🆘



### week1 1/1 🕑

> 💬 逻辑思维能力还是不行，在遇到细节问题一定要沉住气仔细思考，如223题。
>
> 关于223题，简单说一下。这道题本身没什么难度，关键在于仔细分析！！！

- [926 flip-string-to-monotone-increasing](./week1/926-flip-string-to-monotone-increasing.py) `数组` `中等` `有意思的题` ⭐⭐⭐⭐  🤢 
- [932 beautiful-array](./week1/932-beautiful-array.py)  `分治` `中等` `有意思的题` ⭐⭐⭐⭐ 😡 🕑
- [223 rectangle-area](./week1/223-rectangle-area.py) `中等` `数学 ` 🤢 
- [669 trim-a-binary-search-tree](./week1/669-trim-a-binary-search-tree.py) `简单` `二叉树` ⭐ 😃
- [917 reverse-only-letters](./week1/917-reverse-only-letters.py) `简单` `字符串` `双指针` `栈` ⭐  😃



### week1 12/31

- [71 simplify-path](./week1/71-simplify-path.py) `栈` `中等` ⭐⭐  😃
- [173 binary-search-tree-iterator](./week1/173-binary-search-tree-iterator.py) `栈` `中等` ⭐⭐  😃
- [331 verify-preorder-serialization-of-a-binary-tree](./week1/331-verify-preorder-serialization-of-a-binary-tree.py) `栈` `中等` ⭐⭐⭐  😃
- [682 baseball-game](./week1/682-baseball-game.py) `栈` `简单`  ⭐  😃
- [543 diameter-of-binary-tree](week1/543-diameter-of-binary-tree.py) `二叉树` `递归` `简单`  ⭐  😃
