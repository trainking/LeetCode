# 28. 实现 strStr()

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

```
输入: haystack = "hello", needle = "ll"
输出: 2
```

示例 2:

```
输入: haystack = "aaaaa", needle = "bba"
输出: -1
```

说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

## 题解

双指针判断，每个字符开始都从比较

### 代码示例

Python:

```
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        if n == 0:
            return 0
        h_n = len(haystack)
        g = 0
        for h in xrange(0,h_n):
            if (h + n) > h_n:
                break
            t = 0
            while t < n:
                if haystack[h+t] != needle[t]:  # 比较
                    break
                t += 1
            if t == n:  # 判定是否完全相等
                return h
        return -1
```
