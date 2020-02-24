# LeetCode-2020
马上进入2020找实习冲刺阶段，我决定以天为单位，记录每天做的LeetCode习题，方便后期整理。

C++文档神器推荐：*cppreference.chm*

![](./imgs/leetcode-map.jpg)

### 1 LeetCode刷题记录（每日更新）

📅 更新打卡：[2020 - week3 - 2/23](./src/2020-02/README.md)



### 2 各难度典型题目汇总

- 😄 简单题目（典型题目）
  - [949-largest-time-for-given-digits](./week4/949-largest-time-for-given-digits.py) (TODO)
  - [206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)



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
  - [79-word-search](./week4/79-word-search.py) (回溯，TODO)
  - [236-lowest-common-ancestor-of-a-binary-tree](./week4/236-lowest-common-ancestor-of-a-binary-tree.py)  (二叉树递归，TODO)



- 😡 困难题目（值得一看）
  - [52-n-queens-ii](./src/2020-01/week4/52-n-queens-ii.py) (TODO)
  - [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/) `数组`⭐⭐⭐⭐⭐



### 3 其他刷题项目

### 3.1 Daily Problem

（这是另一个每日刷题项目，有空的时候我也会更新）

- [2020-01](DailyProblem/2020-01/)



### 3.2 剑指Offer

总结整理剑指Offer中部分经典题目

- [面试题24. 反转链表（同LeetCode206）](./offer/24-反转链表.md) `链表`
- [面试题03. 数组中重复的数字](./offer/03-数组中重复的数字.md) `哈希`
- [面试题12. 矩阵中的路径（同LeetCode79）](./offer/12-矩阵中的路径.md) `DFS`
- [面试题59 - I. 滑动窗口的最大值（同LeetCode239）](./offer/59-滑动窗口的最大值.md) `滑动窗口`
- [面试题59-ii-队列的最大值](59-ii-队列的最大值.md) `滑动窗口`
- [面试题60. n个骰子的点数](./offer/60-n个色子的点数.md) `DP`
- [面试题52. 两个链表的第一个公共节点](./offer/52-两个链表的第一个公共节点.md) `快慢指针`
- [面试题56 - I. 数组中数字出现的次数](./offer/56-i-数组中数字出现的次数.md) `位运算`
- [面试题57. 和为s的两个数字](./offer/57-和为s的两个数字.md) `对撞指针`
- [面试题14- I. 剪绳子](./offer/14-剪绳子.md) `DP` 
- [面试题53 - I. 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/) `二分` 🕑
- [面试题62. 圆圈中最后剩下的数字](./offer/62-圆圈中最后剩下的数字.md) `约瑟夫环`  `贪心`



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

将最右边一位1置0：

```python
num = num & (num - 1)
```



#### 4.3 二叉树遍历

层序遍历：

```python
def levelOrder(root):
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            count = len(queue)
            cur_line = []
            while count:
                cur = queue.pop(0)
                cur_line.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                count -= 1
            ans.append(cur_line)
        return ans
```

前序遍历非递归写法：

```python
def preOrder(root):
	if not root:
        return []
    ans = []
    stack = [root]
    while stack:
        cur = stack.pop()
        ans.append(cur.val)
        # 这里注意了，是先访问右节点
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return ans
```

中序遍历的非递归写法：

```python
def inOrder(root):
	ans = []
	stack = []
    cur = root
	while cur or stack:
		if cur:
			stack.append(cur.left)
            cur = cur.left
		else:
			cur = stack.pop()
			ans.append(cur.val)
			cur = cur.right
	return ans
```

后序遍历的非递归写法：

```python
# 从根节点开始依次迭代，弹出栈顶元素输出到输出列表中，然后依次压入它的所有孩子节点，按照从上到下、从左至右的顺序依次压入栈中。因为深度优先搜索后序遍历的顺序是从下到上、从左至右，所以需要将输出列表逆序输出。

def postOrder(root):
	if not root:
        return []
    ans = []
    stack = [root]
    while stack:
        cur = stack.pop()
        ans.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return ans[::-1]
```



#### 4.4 排序算法

冒泡排序：

```python
def bubbleSort(arr):
	pass
```

插入排序：

```python
def insertSort(arr):
	pass
```

选择排序：

```python
def selectSort(arr):
	pass
```

快速排序：

```python
def quickSort(arr):
	pass
```

归并排序：

```python
def mergeSort(arr):
	pass
```



#### 4.5 BFS&DFS

BFS解题模板：

```python

```

DFS解题模板：

```python

```



### 5 题目分门别类（TODO）：
**算法类**：

- 分治、二分

  - [面试题53 - I. 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/) 

- 排序算法：快速排序、归并排序、计数排序

  - 冒泡排序
  - 快速排序
  - 归并排序

- 搜索算法：回溯、递归、深度优先遍历，广度优先遍历，二叉搜索树等

  - DFS
  - BFS

- *图论：最短路径、最小生成树

- 动态规划：背包问题、最长子序列

  - [面试题14- I. 剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)
  - [面试题60. n个骰子的点数](./offer/60-n个色子的点数.md) 

- 位运算

  - 异或：相同为0，不同为1
  - [136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number/)
    - [137. 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii/)
    - [260. 只出现一次的数字 III](https://leetcode-cn.com/problems/single-number-iii/)
  - 与
  - 左移/右移
  - 综合
  
- 贪心

  - [面试题62. 圆圈中最后剩下的数字](./offer/62. 圆圈中最后剩下的数字.md) 

- 数学/逻辑/规律：

  - [794. 有效的井字游戏](https://leetcode-cn.com/problems/valid-tic-tac-toe-state/)
  - [面试题61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)
  - [面试题62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)
  
  

**数据结构类**：

- 数组

  - 快慢指针
  - 对撞指针
    - [面试题57. 和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/)
  - 滑动窗口
    - [面试题57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)
    - [面试题59 - I. 滑动窗口的最大值（同LeetCode239）](./offer/59-滑动窗口的最大值.md)
    - [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/) 🕑
    - [30. 串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/) 🕑
    - [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/) 🕑
    - [159. 至多包含两个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/) 🕑
    - [209. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/) 🕑
    - [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)
    - [340. 至多包含 K 个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/) 🕑
    - [438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/) 🕑
    - [567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/) 🕑
    - [632. 最小区间](https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/) 🕑
    - [727. 最小窗口子序列](https://leetcode-cn.com/problems/minimum-window-subsequence/) 🕑

- 链表

  - 链表反转

- 栈与队列

- 哈希表

- 堆：最大堆 ／ 最小堆

  - 优先队列

- 二叉树 

  - 递归
    - [687. 最长同值路径](https://leetcode-cn.com/problems/longest-univalue-path/)
    - [面试题68 - I. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/er-cha-shu-jiu-yong-di-gui-python-by-wonanut/)
  - 遍历
    - 二叉树的层次遍历：[102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
    - 二叉树的先序遍历：[144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)
    - 二叉树的中序遍历：
      - [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
      - [897. 递增顺序查找树](https://leetcode-cn.com/problems/increasing-order-search-tree/) 
    - 二叉树的后序遍历：[145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
    - 二叉树的垂序遍历：[987. 二叉树的垂序遍历](https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree/)

- 图：最近公共祖先、并查集

  - DFS
  - BFS
  - 并查集

- 字符串：前缀树（字典树） ／ 后缀树




**系列问题**

- 股票问题：
  - [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) 🕑
  - [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) 🕑
  - [123. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/) 🕑
  - [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/) 🕑
  - [188. 买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/submissions/) 🕑
  - [714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/submissions/) 🕑



## Top题目进度

- Top 100 Linked Questions [0%]
- Top Interview Questions [0%]



#### 优秀LeetCode题解传送门：https://github.com/wonanut/leetcode



## 目录

- [2020 - week1](./src/2020-01/week1/)
- [2020 - week2](./src/2020-01/week2/)
- [2020 - week3](./src/2020-01/week3/)