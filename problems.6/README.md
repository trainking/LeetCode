# ZigZag Conversion

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
`convert("PAYPALISHIRING", 3)` should return `"PAHNAPLSIIGYIR"`.

## Solution

形成这样一个`Z`型字符串，其实通过数学归纳法，可以得出一个简单的公式。其实本质上是求复杂了两种规则。竖线排列和折线排列。

### 竖线排列
竖线排列的位置是位置顺序变更n个，变更index是行。

### 折线排列
折线排列是每行一个，排列n-2列，变更index为列。
