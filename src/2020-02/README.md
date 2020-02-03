## 2020年二月LeetCode解题笔记

Howard Wonanut 2020刷题 / 过于简单的题目不做记录

##### 😃简单题     🤢只会暴力    😡毫无头绪    ⭐题目难度量化    🆕当前周     🕑待整理       ✅已整理      🆘未解决



### week1 2/3

- [384 shuffle-an-array](./week1/384-shuffle-an-array.py) `洗牌算法` `中等` ⭐⭐⭐  😃

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

