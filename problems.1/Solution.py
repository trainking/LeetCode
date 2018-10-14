class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for n in range(0, len(nums)):
            m[nums[n]] = n

        for n in range(0, len(nums)):
            t = target - nums[n]
            if(m.has_key(t) and m.get(t) != n):
                return [n, m[t]]
