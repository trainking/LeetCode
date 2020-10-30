# 16.最接近的三数之和

给定一个包括`n`个整数的数组`nums`和 一个目标值`target`。找出`nums`中的三个整数，使得它们的和与`target`最接近。返回这三个数的和。假定每组输入只存在唯一答案。

**实例**

```
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
```
**提示**

* `3 <= nums.length <= 10^3`
* `-10^3 <= nums[i] <= 10^3`
* `-10^4 <= target <= 10^4`

## 题解

假设三个数a,b,c，当a确定时，其实求的b+c的和与`target-a`最接近结果，利用类似**选择排序**的思路，保存最接近的三数之和，遍历找出。

**如何去除重复呢？**

如果将`nums`先升序，则通过跳过连续相同值的方式去重。

同时，b,c的选取可以通过判定与`target`的大小比较，跳动指针搜索。

## 代码示例

Python：

```
lass Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in xrange(0, len(nums)):
            if i > 0 and nums[i] == num[i-1]:   # 去重，跳过连续相同数
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                su = nums[i] + nums[start] + nums[end]
                if  abs(target - su) < abs(target - ans):  # 比较绝对值，确定最接近数
                    ans = su
                # 根据最接近数与target的比较，确定移动的指针
                if su > target:
                    end -= 1
                elif su < target:
                    start +=1 
                else:
                    return ans

        return ans
```

