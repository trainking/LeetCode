# 18.四数之和

给定一个包含`n`个整数的数组`nums`和一个目标值`target`，判断`nums`中是否存在四个元素`a，b，c`和`d`，使得`a + b + c + d`的值与`target`相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

**示例：**

给定数组`nums = [1, 0, -1, 0, -2, 2]`，和 `target = 0`。

满足要求的四元组集合为：

```
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

## 题解

基本原理与三数之和类似，增加一层循环

## 代码示例

Python:

```
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if not nums:
            return result
        len_nums = len(nums)
        if len_nums < 4:
            return result
        nums.sort()
        for i in range(0, len_nums - 3):
            # 判断当前数与前一个数是否相通,如果相通则跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            _min = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
            if _min > target:
                break
            _max = nums[i] + nums[len_nums - 1] + nums[len_nums - 2] +nums[len_nums - 3]
            if _max < target:
                continue
            for j in range(i+1, len_nums - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                h = j + 1
                k = len_nums -1 
                _min = nums[i] + nums[j] + nums[h] + nums[h + 1]
                if _min > target:
                    break
                _max = nums[i] + nums[j] + nums[k] + nums[k - 1]
                if _max < target:
                    continue
                while h < k:
                    cur = nums[i] + nums[j] + nums[h] + nums[k]
                    if cur == target:
                        result.append([nums[i], nums[j], nums[h], nums[k]])
                        h += 1
                        while h < k and nums[h] == nums[h -1]:
                            h +=1 
                        k -= 1
                        while h < k and nums[k] == nums[k + 1]:
                            k -= 1
                    elif cur > target:
                        k -= 1
                    else :
                        h += 1

        return result
```
