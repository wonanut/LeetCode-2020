# LeetCode-2020
马上进入2020找实习冲刺阶段，我决定以天为单位，记录每天做的LeetCode习题，方便后期整理。

![](./imgs/leetcode-map.jpg)

### 1 LeetCode刷题记录（每日更新）

📅 更新打卡：[2020 - week1 - 1/21](./src/2020-01/README.md)



### 2 各难度典型题目汇总

- 😄 简单题目（典型题目）
  - [949-largest-time-for-given-digits](./week4/949-largest-time-for-given-digits.py) (TODO)



- 🤢 中等难题（题目本身不是很难，但是并不一定写得出来）
  - [838 push-dominoes](./puzzles/838-push-dominoes.md) (TODO)
  - [932 beautiful-array]()(TODO)
  - [334 increasing-triplet-subsequences](./week2/334-increasing-triplet-subsequence.py) (TODO)
  - [838 push-dominoes](./week1/838-push-dominoes.py) (TODO)
  - [984 string-without-aaa-or-bbb](./week1/984-string-without-aaa-or-bbb.py) (TODO)
  - [959 regions-cut-by-slashes](./week2/959-regions-cut-by-slashes.py) (并查集，TODO)
  - [96-unique-binary-search-trees](./week3/96-unique-binary-search-trees.py) (二叉搜索树，TODO)
  - [96-unique-binary-search-trees](./week3/96-unique-binary-search-trees.py) (二叉搜索树，TODO)
  - [399-evaluate-division](./src/2020-01/week3/399-evaluate-division.py) (并查集，TODO)



- 😡 困难题目（值得一看）





### 3 Daily Problem

（这是另一个每日刷题项目，有空的时候我也会更新）

- [2020-01](DailyProblem/2020-01/)





### 4 常用解题方法总结

#### 4.1 并查集

并查集是一种树形数据结构，用于处理一些非连通子图的合并以及查询问题，主要使用`Union`以及`find`两个方法定义了该数据结构的相关操作：

- Find：确定给定元素属于哪个子集，可以用于确定两个元素是否属于同一个子集；
- Union：将两个子集合并成同一个集合。

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

并查集经典题目：

- [959 regions-cut-by-slashes](./src/2020-01/week2/959-regions-cut-by-slashes.py) (TODO)
- [399-evaluate-division](./src/2020-01/week3/399-evaluate-division.py) (TODO)



#### 4.2 位运算

检查数x是否为2的幂：

```python
x > 0 and x & (x - 1) == 0
```



#### 4.3 二叉搜索树递归





### 5 题目分门别类（TODO）：
**算法类**：

- 基础技巧：分治、二分、贪心

- 排序算法：快速排序、归并排序、计数排序

- 搜索算法：回溯、递归、深度优先遍历，广度优先遍历，二叉搜索树等

- 图论：最短路径、最小生成树

- 动态规划：背包问题、最长子序列

  

**数据结构类**：

- 数组与链表

- 栈与队列

- 哈希表

- 堆：最大堆 ／ 最小堆

- 二叉树 

- 图：最近公共祖先、并查集、图论

- 字符串：前缀树（字典树） ／ 后缀树

  

## Top题目进度

- Top 100 Linked Questions [0%]
- Top Interview Questions [0%]



#### 优秀LeetCode题解传送门：https://github.com/wonanut/leetcode



## 目录

- [2020 - week1](./src/2020-01/week1/)
- [2020 - week2](./src/2020-01/week2/)
- [2020 - week3](./src/2020-01/week3/)