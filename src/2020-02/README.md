## 2020年二月LeetCode解题笔记

Howard Wonanut 2020刷题 / 过于简单的题目（没有星星标记）只有到官网链接

##### 😃简单题     🤢只会暴力    😡毫无头绪    ⭐题目难度量化    🆕当前周     🕑待整理       ✅已整理      🆘未解决

*剑指offer系列题目题解均在`Leetcode题解`。



### 2月做题记录表

| 日期 | 数目 | 日期 | 数目 | 日期 | 数目 | 日期 | 数目 | 日期  | 数目 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- | ---- |
| 2/1  | 0    | 2/8  | 3    | 2/15 | 0    | 2/22 | 6    | 2/29  | -    |
| 2/2  | 0    | 2/9  | 0    | 2/16 | 8    | 2/23 | -    | total | 62   |
| 2/3  | 7    | 2/10 | 0    | 2/17 | 4    | 2/24 |      |       |      |
| 2/4  | 2    | 2/11 | 0    | 2/18 | 3    | 2/25 |      |       |      |
| 2/5  | 0    | 2/12 | 0    | 2/19 | 13   | 2/26 |      |       |      |
| 2/6  | 1    | 2/13 | 0    | 2/20 | 8    | 2/27 |      |       |      |
| 2/7  | 0    | 2/14 | 0    | 2/21 | 7    | 2/28 | -    |       |      |



### 2 月解题能力评估

| 类型         | 水平                      | 类型      | 水平                      |
| ------------ | ------------------------- | --------- | ------------------------- |
| 数组/矩阵    | [--------------------] ?% | 动态规划  | [--------------------] ?% |
| 链表         | [--------------------] ?% | 二分查找  | [--------------------] ?% |
| 二叉树       | [--------------------] ?% | 贪心算法  | [--------------------] ?% |
| 深度优先搜索 | [--------------------] ?% | 回溯算法  | [--------------------] ?% |
| 广度优先搜索 | [--------------------] ?% | 排序算法  | [--------------------] ?% |
| 栈/队列      | [--------------------] ?% | 分治思想  | [--------------------] ?% |
| 堆           | [--------------------] ?% | 并查集/图 | [--------------------] ?% |
| 其他         | [--------------------] ?% | 位运算    | [--------------------] ?% |



### week1 2/3 🆕

【1】[384 shuffle-an-array](./week1/384-shuffle-an-array.py) `洗牌算法` `中等` ⭐⭐⭐  😃

python中生成随机数的函数：

```python
# 1 random.randint(a,b)函数返回[a,b]之间的随机整数
import random
random.randint(a, b)

# 2 numpy.random.randint(a,b)返回[a,b)之间的随机整数
import numpy as np
np.random.randint(a, b)
```

洗牌算法模板：

```python
def shuffle(nums):
	right = len(nums) - 1
    while right > 0:
        rand = random.randint(0, right)
        nums[rand], rand[right] = nums[right], nums[rand]
        right -= 1
    return nums
```



【2】[733-flood-fill](./week1/733-flood-fill.py) `dfs` `简单` ⭐

> 💬 733题考察深度优先搜索，需要考虑特殊情况：更换的值和原来的值相同则直接返回，否则会进入死循环



【3】[463-island-perimeter](./week1/463-island-perimeter.py) `二维数组` `简单` ⭐⭐⭐ 🤢

> 💬 467使用dfs大题小作了，容易得到$result=4*count-2*connect$，难点在于如何得到相邻的墙壁的个数connect：对于每一个值为1的方块，计算其左边和上边为1的方块的个数。



【4】[747-largest-number-at-least-twice-of-others](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/)



【5】[529-minesweeper](./week1/529-minesweeper.py) `二维数组` `中等` ⭐⭐⭐⭐ 🕑

> 💬 529题本身没什么难的，就是一个dfs问题，但是我的代码逻辑除了些问题，这道题很经典，好好整理！



【6】[532-k-diff-pairs-in-an-array](./week1/532-k-diff-pairs-in-an-array.py) `数组` `简单`  ⭐⭐⭐⭐ 🕑

Python数组排序函数：

```python
arr = [3,4,5,2,1]

# 1 arr.sort()直接对原始数组排序
arr.sort()
print(arr)	# arr将变为[1,2,3,4,5]

# 2 r = sorted(arr)返回排好序的数组，原始数组不变
r = sorted(arr) # arr不变，r=[1,2,3,4,5]
```



【7】[551-student-attendance-record-i](./week1/551-student-attendance-record-i.py) `数组` `简单` ⭐

Python字符串常用函数：

```python
s = "abcddefg"

# 1 统计字符串数组中字符出现次数：
s.count('a') 

# 2 字符串匹配
"dd" in s
```



### week1 2/4 🆕

【8】[264-ugly-number-ii](./week1/264-ugly-number-ii.py) `DP` `中等` 🆘

本来想着使用bfs或者dfs生成所有的值，但是后来发现不行，复杂度太高超时（不过有个小技巧：在本地生成前1690个数据后直接把结果存起来）。后来看官方提示，这道题应该用DP解法优化。

【9】[263-ugly-number](./week1/263-ugly-number.py) `数学` `简单` ⭐⭐



### week1 2/6 🆕

【10】[947-most-stones-removed-with-same-row-or-column](./week1/947-most-stones-removed-with-same-row-or-column.py) `DP` `中等`

【11】[367-valid-perfect-square](./week1/367-valid-perfect-square.py) `二分` `中等` ⭐⭐



### week1 2/8 🆕

【12】[1048-longest-string-chain](./week1/1048-longest-string-chain.py) `DP` `中等` ⭐⭐⭐ 🕑

```python
# 获取dict的值列表
l = d.values()

# python dict.get()函数
# Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
dict = {'Name': 'Zara', 'Age': 27}

print "Value : %s" %  dict.get('Age')
# Value : 27

print "Value : %s" %  dict.get('Sex', "Never")
# Value : Never
```

【13】[802-find-eventual-safe-states](./week1/802-find-eventual-safe-states.py) `DFS` `中等`

【14】[201-bitwise-and-of-numbers-range](./week1/201-bitwise-and-of-numbers-range.py) `位运算` `中等` ⭐⭐⭐ 🕑

【15】[191-number-of-1-bits](./week1/191-number-of-1-bits.py) `位运算` `简单` ⭐ 🕑



### week2 2/16 🆕

【16】[面试题03. 数组中重复的数字]() `剑指offer` ⭐⭐ 🕑

【17】[面试题04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/er-wei-shu-zu-si-xiang-hen-zhong-yao-pythonjie-fa-/) `剑指offer` ⭐⭐

【18】[面试题07. 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/fen-zhi-si-xiang-pythonban-ben-jie-da-by-wonanut/) `剑指offer` `中等` ⭐⭐

【19】[752-open-the-lock](./week2/752-open-the-lock.py) `中等` ⭐⭐

使用Python中`set`和`list`的一点点小区别

```python
# 虽然python中的set和list都可以使用 in 用来查找，但是其时间复杂度是不一样的！
# 在list中使用 in 时间复杂度为O(n)
# 在set中使用 in 时间复杂度为O(1)！
```

【20】[面试题68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/er-cha-shu-ji-ben-du-shi-di-gui-pythonjie-fa-by-wo/) `剑指offer` ⭐⭐⭐ 🕑

【21】[面试题68 - I. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/er-cha-shu-jiu-yong-di-gui-python-by-wonanut/) `剑指offer` ⭐⭐

【22】[面试题67. 把字符串转换成整数](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/) `剑指offer` ⭐

【23】[面试题66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/qian-hou-bian-li-pythonban-by-wonanut/) `剑指offer` ⭐⭐⭐ 🕑



### week3 2/17 🆕

【24】[面试题65. 不使用加减乘除做加法](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/) `剑指offer` **⭐⭐⭐⭐⭐** 🕑

~~【25】[5342. 最多可以参加的会议数目](https://leetcode-cn.com/contest/weekly-contest-176/problems/maximum-number-of-events-that-can-be-attended/)~~ `周赛` `中等` ⭐⭐⭐ 🆘

【26】[面试题11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)  `剑指offer` `困难` ⭐⭐⭐⭐⭐ 🕑

~~【27】[31. 下一个排列](https://leetcode-cn.com/problems/next-permutation/)~~ 🆘

【28】[154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/) `数组`⭐⭐⭐⭐⭐

【29】[153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) `数组`⭐⭐⭐

 

### week3 2/18 🆕

【30】[面试题65. 不使用加减乘除做加法](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/) `剑指offer` **⭐⭐⭐⭐⭐** 🕑

【31】[125. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)

python判断字符串的一些方法：

```python
# str为字符串
str.isalnum() # 所有字符都是数字或者字母
str.isalpha() # 所有字符都是字母
str.isdigit() # 所有字符都是数字
str.islower() # 所有字符都是小写
str.isupper() # 所有字符都是大写
str.istitle() # 所有单词都是首字母大写，像标题
str.isspace() # 所有字符都是空白字符、\t、\n、\r
```

C++中vector定义二维数组

```C++
#include <vector>

// 定义一个10行5列的二维数组, vector默认值为0
vector<vector<int>> vec(10);
for (int i = 0; i < 10; i++) {
    vec[i].resize(5);
}
```

【32】[209. 长度最小的子数组](./src/209-minimum-size-subarray-sum.md) 

python中使用int最大值：

```
sys.maxint
```

【33】[3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/) 🆘

~~【34】[438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/) 🆘~~

【35】[76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)



### week3 2/19 🆕二叉树刷分日

【36】[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/) `困难` `滑动窗口`⭐⭐⭐⭐⭐

【37】[102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) `队列`⭐⭐

【38】[107. 二叉树的层次遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/) `队列`⭐

【39】[637. 二叉树的层平均值](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/) `队列`⭐

【40】[94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) `栈`⭐⭐⭐

【41】[144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/) `栈`⭐

【42】[145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/) `困难` `辅助栈`⭐⭐⭐⭐

【43】[429. N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/) `队列`⭐⭐

【44】[589. N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/) `栈`⭐

【45】[590. N叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/) `栈`⭐⭐⭐⭐

【46】[105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) `递归`⭐⭐

~~【47】[889. 根据前序和后序遍历构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)~~ ⭐⭐⭐ 🆘

【48】[897. 递增顺序查找树](https://leetcode-cn.com/problems/increasing-order-search-tree/) `在原节点上修改` ⭐⭐⭐⭐

【49】[面试题32 - III. 从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/) `队列`⭐⭐



### week3 2/20 🆕

【50】[987. 二叉树的垂序遍历](https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree/) `DFS`⭐⭐⭐

python中的sort函数可以指定对多个key进行排序：

```python
# 先对最右边元素进行排序，依次往左
arr.sort(key = lambda x: (x[1], x[2], x3]))
```

【51】[687. 最长同值路径](./week3/687-longest-univalue-path.py) `递归`⭐⭐⭐

【52】[938. 二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst/) `递归`⭐

【53】[794. 有效的井字游戏](https://leetcode-cn.com/problems/valid-tic-tac-toe-state/) `逻辑`⭐⭐⭐⭐

【54】[面试题60. n个骰子的点数](./offer/60-n个色子的点数.md) `DP`⭐⭐⭐⭐

【55】[面试题13. 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/) `DFS`⭐

【56】[面试题50. 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/) `hash`⭐

【57】[面试题55 - I. 二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/) `递归`⭐



### week3 2/21 🆕

【58】[面试题14- I. 剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/) `DP`⭐⭐⭐

【59】[面试题52. 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/) `链表` `快慢指针`⭐⭐

【60】[面试题55 - II. 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/) `递归`⭐

【61】[面试题57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/) `滑动窗口`⭐

【62】[面试题59 - II. 队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/) `滑动窗口` ⭐⭐

【63】[面试题57. 和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/) `对撞指针`⭐

【64】[面试题56 - I. 数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/) `位运算-异或`⭐⭐⭐⭐



### week3 2/22 🆕



还是用C++写题目吧，以后转战C++，用VS调试。

`今日总结`

1. 递归修改指针的问题一定要小心，很容易陷入死循环，如114题。
2. 一定要耐心认真读题！！！

| 编号   | 题目                                                         | 标签   | 星标  | 挑战 |
| ------ | ------------------------------------------------------------ | ------ | ----- | ---- |
| 65     | [114. 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/) | `递归` | ⭐⭐⭐⭐⭐ | 失败 |
| 66     | [129. 求根到叶子节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/) | `递归` | ⭐⭐    | 成功 |
| ~~67~~ | ~~[字节校园学习挑战赛0221](https://github.com/wonanut/LeetCode-2020/blob/master/zjxy/0221.cpp)~~ | `DP`   | ⭐⭐⭐   | 失败 |
| 68     | [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/solution/55-by-ikaruga/) | `贪心` | ⭐⭐⭐   | 失败 |
| 69     | [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | `二分` | ⭐⭐    | 成功 |
| 70     | [面试题53 - I. 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/) | `二分` | ⭐⭐    | 成功 |
| 71     | [面试题61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/) | `逻辑` | ⭐⭐    | 失败 |



### week3 2/23 🆕

`今日总结`

1. 约瑟夫环问题用模拟的方法解决不难，难在如何不用模拟的方法解决，已经做题解。
2. 动态规划的题目仔细分析，76号题(字节校园)应该是dp问题，一开始想不到怎么做。

| 编号 | 题目                                                         | 标签       | 星标 | 挑战 |
| ---- | ------------------------------------------------------------ | ---------- | ---- | ---- |
| 72   | [面试题62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/) | `约瑟夫环` | ⭐⭐⭐⭐ | 成功 |
| 73   | [31. 下一个排列](https://leetcode-cn.com/problems/next-permutation/) |            |      |      |
| 74   | [889. 根据前序和后序遍历构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) |            | ⭐⭐⭐  |      |
| 75   | [5342. 最多可以参加的会议数目](https://leetcode-cn.com/contest/weekly-contest-176/problems/maximum-number-of-events-that-can-be-attended/) |            |      |      |
| 76   | [字节校园学习挑战赛0221](https://github.com/wonanut/LeetCode-2020/blob/master/zjxy/0221.cpp) | `DP`       | ⭐⭐⭐  | --   |
| 77   | [438. 找到字符串中所有字母异位词](./week3/438-找到字符串中所有字母异位词.md) | `滑动窗口` | ⭐⭐⭐  | 失败 |
| 78   | [面试题 10.01. 合并排序的数组](https://leetcode-cn.com/problems/sorted-merge-lcci/) | `三指针`   | ⭐    | 成功 |
| 79   | [字节校园学习挑战赛0223](https://github.com/wonanut/LeetCode-2020/blob/master/zjxy/0223.cpp) | `DP`       | ⭐    | 成功 |
| 80   | 字节校园学习挑战赛0219                                       | `位运算`   |      | 失败 |

