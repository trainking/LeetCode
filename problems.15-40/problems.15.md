# 15.三数之和

给你一个包含`n`个整数的数组`nums`，判断`nums`中是否存在三个元素`a，b，c`，使得`a + b + c = 0 ？`请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

**示例**

```
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

## 题解

分析一下，因为三数之和要等于0，其实它的解有几种情况：

+ [0,0,0]
+ [-a, 0, a]
+ [-a, b, c]
+ [-a, -b, c]

因此只要分支为这四种策略，搜索需要的结果即可。

**如何保证没有重复的结果呢？**

改变数据的结构，使用字典做映射，第一个首先字典Key组合中，没有重复的结果，标记一个元素出现的次数，求解时再减去次数，保证找值不重复选取

## 代码示例

Python:

```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        _l_nums = {}
        _r_nums = {}
        _m_n = 0
        result = []

        for n in nums:
            if n > 0:
                if _r_nums.has_key(n):
                    _r_nums[n] += 1
                else:
                    _r_nums[n] = 1
            elif n == 0:
                _m_n += 1
            else:
                if _l_nums.has_key(n):
                    _l_nums[n] += 1
                else:
                    _l_nums[n] = 1

        if _m_n >= 3:
            result.append([0, 0, 0])

        if _m_n > 0:
            for _r in _r_nums.keys():
                t = 0 - _r
                if _l_nums.has_key(t):
                    result.append([t, 0, _r])
        _temp_result = {}

        for _r in _r_nums.keys():
            target = 0 - _r
            for _l in _l_nums.keys():
                t = target - _l
                if t == _l:
                    if  _l_nums[_l] > 1:
                        g = [_l, _l, _r]
                        g.sort()
                        _temp_result[hash(str(g))] = g
                else:
                    if _l_nums.has_key(t):
                        g = [_l, t, _r]
                        g.sort()
                        _temp_result[hash(str(g))] = g


        for _l in _l_nums.keys():
            target = 0 - _l
            for _r in _r_nums.keys():
                t = target - _r
                if t == _r:
                    if  _r_nums[_r] > 1:
                        g = [_r, _r, _l]
                        g.sort()
                        _temp_result[hash(str(g))] = g
                else:
                    if _r_nums.has_key(t):
                        g = [_r, t, _l]
                        g.sort()
                        _temp_result[hash(str(g))] = g

        _val = _temp_result.values()
        result.extend(_val)
        return result
```
