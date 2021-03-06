# Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

**Example:**

```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

这题的的关键点在于两个方面，横向和纵向，横向取所有的间隔，纵向取最短的一块短板。最直观的方法，可以通过最简单的方式获得。

**解法一:**

最直接的方式，就是通过遍历看比较所有的结果。
```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        l = len(height)
        result = 0
        while left < right:
            h = height[left] if height[left] < height[right] else height[right]
            r = (right - left) * h
            result = result if result > r else r
            if right == l - 1:
                left += 1
                if left < l - 2:
                    right = left + 1
            else:
                right += 1
        return result 
```

这种解法的缺点是时间复杂度太高，超过时限，这是个***O(n2)***的算法。

**解法二:**

上一个解法我已经摸到门道了，由两个下标来标识矩形。但是我上一个算法是从头遍历到尾的，其实可以通过两个下标从左右不同的两边开始移动，因为
每个元素间的间隔是恒定的，所以开始就从两边开始，最容易找出最大的区域。

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        l = len(height)
        right = l - 1
        result = 0
        while left < right:
            h = height[left] if height[left] < height[right] else height[right]
            r = (right - left) * h
            result = result if result > r else r
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result 
```

我本以为这是最佳的解法了，结果还有更高的效率的，但是这只是对python语言的性能上的优化了。只是将中间两步计算方式，改为python内置的`max`和`min`方法，得到性能上的提升。