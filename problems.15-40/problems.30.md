# 30. 串联所有单词的子串

给定一个字符串`s`和一些长度相同的单词`words`。找出`s`中恰好可以由`words`中所有单词串联形成的子串的起始位置。

注意子串要与`words`中的单词完全匹配，中间不能有其他字符，但不需要考虑`words`中单词串联的顺序。

 

示例 1：

```
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
```

示例 2：

```
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
```

## 题解

### 代码示例

Python:

```
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        l_s = len(s)
        t_w = len(words)
        ans = []
        if t_w == 0 or l_s == 0:
            return ans
        l_w = len(words[0])
        if l_s < (t_w * l_w) :
            return ans
        word_map = {}
        for w in words:
            if w in word_map:
                word_map[w] += 1
            else:
                word_map[w] = 1
        for i in xrange(0, len(s) - (t_w * l_w) + 1):
            c = 0
            j = i
            word_map_copy = word_map.copy()
            while c < t_w:
                c_w = s[j:j+l_w]
                if c_w in word_map_copy and word_map_copy[c_w] != 0:
                    c += 1
                    word_map_copy[c_w] -=1
                    j += l_w
                else:
                    break

                if c == t_w:
                    ans.append(i)

        return ans
```
