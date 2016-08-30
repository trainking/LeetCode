class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numslen = len(nums)
        leftIndex = 0
        rightIndex = numslen - 1
        while leftIndex < rightIndex:
            midIndex = (leftIndex + rightIndex) / 2
            if nums[midIndex] == target:
                return midIndex
            if nums[midIndex] < target:
                leftIndex = midIndex + 1
            else:
                rightIndex = midIndex - 1

        if nums[leftIndex] < target:
            return leftIndex+1
        else:
            return leftIndex
