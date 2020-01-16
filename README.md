# LeetCode-2020
马上进入2020找实习冲刺阶段，我决定以天为单位，记录每天做的LeetCode习题，方便后期整理。



### 1 LeetCode刷题记录（每日更新）

📅 更新打卡：[2020 - week1 - 1/16](./src/2020-01/README.md)



### 2 各难度典型题目汇总

- 😄 简单题目（典型题目）



- 🤢 中等难题（题目本身不是很难，但是并不一定写得出来）
  - [838 push-dominoes](./puzzles/838-push-dominoes.md) (TODO)
  - [932 beautiful-array]()(TODO)
  - [334 increasing-triplet-subsequences](./week2/334-increasing-triplet-subsequence.py) (TODO)
  - [838 push-dominoes](./week1/838-push-dominoes.py) (TODO)
  - [984 string-without-aaa-or-bbb](./week1/984-string-without-aaa-or-bbb.py) (TODO)
  - [959 regions-cut-by-slashes](./week2/959-regions-cut-by-slashes.py) (并查集，TODO)



- 😡 困难题目（值得一看）





### 3 Daily Problem

（这是另一个每日刷题项目，有空的时候我也会更新）

- [2020-01](DailyProblem/2020-01/)





### 4 算法思路总结

#### 4.1 并查集

并查集核心代码：

```python
# 并查集模板Python代码
class UnionSet(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, num):
        if self.parent[num] == num:
            return self.parent[num]
        return self.find(self.parent[num])
    
    def union(self, num1, num2):
        self.parent[self.find(num1)] = self.find(num2)

    def count(self):
        return len([1 for i, num in enumerate(self.parent) if num == i])
```







### 5 题目分门别类（TODO），具体参考下图：
![](./imgs/leetcode-map.jpg)

**算法类**：

- 基础技巧：分治、二分、贪心

- 排序算法：快速排序、归并排序、计数排序

- 搜索算法：回溯、递归、深度优先遍历，广度优先遍历，二叉搜索树等

- 图论：最短路径、最小生成树

- 动态规划：背包问题、最长子序列

  

**数据结构类**：

- 数组与链表：单 / 双向链表

- 栈与队列

- 哈希表

- 堆：最大堆 ／ 最小堆

- 树与图：最近公共祖先、并查集

- 字符串：前缀树（字典树） ／ 后缀树

  

## Top题目进度

- Top 100 Linked Questions [0%]
- Top Interview Questions [0%]



#### 优秀LeetCode题解传送门：https://github.com/wonanut/leetcode



## 目录

- [2020 - week1](./src/2020-01/week1/)
- [2020 - week2](./src/2020-01/week2/)
- [2020 - week3](./src/2020-01/week3/)