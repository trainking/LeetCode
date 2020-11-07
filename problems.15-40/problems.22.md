# 22. 括号的生成

数字`n`代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且**有效的**括号组合。

**示例:**

```
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

```

## 题解

两层递归，一层找左边，一层找右边，再合并结果


### 代码示例

Python：

```
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return ['']
        ans = []
        for c in xrange(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
```
