# 20.有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

```
输入: "()"
输出: true
```
示例 2:

```
输入: "()[]{}"
输出: true
```

示例 3:

```
输入: "(]"
输出: false
```

示例 4:

```
输入: "([)]"
输出: false
```

示例 5:

```
输入: "{[]}"
输出: true
```


## 题解

利用栈的特性，判断栈顶元素和后进来元素配对，如果最终栈为空，则所有配对成功，如果非空，不能全部非对，如果大于一半入栈了，也不能配对成功。

### 代码示例

```
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        _map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for g in s:
            if len(stack)  == 0:
                stack.append(g)
            else:
                if _map.has_key(stack[-1]) and g == _map[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(g)
            # 入栈大于一半，不能配对
            if len(stack) > (len(s) / 2):
                return False
        # 判断最后是否仍然有未配对元素，不能出栈
        return len(stack) == 0
```