#  Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

## 优化算法

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        for i in strs:
            if not strs:
                return ""
            
        min_len=min([len(x) for x in strs])
        
        if min_len==0:
            return ""
        
        res=""
        for i in range(min_len):
            #extract ith char from all strings
            n=len(set([x[i] for x in strs]))
            if n==1:
                res+=strs[0][i]
            else:
                return res
        
        return res
```
