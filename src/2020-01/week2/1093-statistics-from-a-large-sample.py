"""
1093：大样本统计
难度：中等
标签：数学、加法上溢出
评价：这道题看起来不难，而且判题器判的也比较松，在求解均值的时候需要解决上溢出的问题吧？
python好像不用考虑上溢出的问题还是啥不清楚，反正我没有考虑上溢出也通过了。这道题最麻烦的在求中位数，当抽样次数为偶数时需要额外考虑一种情况。
"""

class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        ans = [float(0) for i in range(5)]
        for i in range(len(count)):
            if count[i] > 0:
                ans[0] = i
                break
        for j in range(len(count) - 1, -1, -1):
            if count[j] > 0:
                ans[1] = j
                break
        temp_max, temp_idx = 0, -1
        temp_count, temp_sum = 0, 0.0
        for i in range(len(count)):
            temp_count += count[i]
            temp_sum += i * count[i]
            if count[i] > temp_max:
                temp_max, temp_idx = count[i], i
        ans[4] = temp_idx
        ans[2] = temp_sum / temp_count

        cur_count = 0
        mid = temp_count // 2
        if (temp_count >> 1) & 0x1:
            for i in range(len(count)):
                if cur_count < mid and cur_count + count[i] > mid:
                    ans[3] = i
                    break
                cur_count += count[i]
        else:
            for i in range(len(count)):
                if cur_count < mid and cur_count + count[i] > mid:
                    ans[3] = i
                    break
                elif cur_count == mid:
                    for j in range(i, len(count)):
                        if count[j] > 0:
                            break
                    ans[3] = (i + j - 1) / 2.0
                cur_count += count[i]
        return ans
        
