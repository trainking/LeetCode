# 27. 移除元素

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并**原地**修改输入数组。

元素的顺序可以改变。**你不需要考虑数组中超出新长度后面的元素**

## 题解

暴力删除

Pyhton:

```
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
```

在Python中因为实现了`del`的缘故，所以很方便，但是其他语言中可以运用交换位置的思想

Python：

```
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in xrange(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i+1
        return i
```

C：

```
int removeElement(int* nums, int numsSize, int val) {
    if (numsSize == 0) {
        return numsSize;
    }

    int i,j;
    i = 0;
    for (j = 0; j < numsSize; j ++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i ++;
        }
    }
    return i;
}
```
