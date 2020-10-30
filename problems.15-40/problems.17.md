# 17.电话号码的字母组合

给定一个仅包含数字`2-9`的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

|1-!@#|2-abc|3-def|
|:--|:--|:--|
|4-ghi|5-jkl|6-mno|
|7-pqrs|8-tuv|9-wxyz|

**示例**

```
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

## 题解

这题没难度，想你换组合而已，需要构造一个数字和字符集合的对应表，我这使用了一下ansi编码的特性。

## 代码示例

Python:

```
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        k_mp = {}
        v = 97
        for i in range(2, 10):
            _r = []
            g = 3
            if i == 7 or i ==9 :
                g = 4
            for p in range(g):
                _r.append(chr(v + p))
            v += g
            k_mp[i] = _r
        d_r = tuple(digits)
        if len(d_r) == 0:
            return None
        p_r = []
        for d in d_r:
            p_r.append(k_mp[int(d)])
        result = [""]
        for pool in p_r:
            result = [x + str(y) for x in result for y in pool]
        return result
```
