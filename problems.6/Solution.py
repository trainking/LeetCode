# coding: utf-8

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        _map = [[] for x in xrange(numRows)]  # 结果集
        _len = len(s)

        i = 0
        while(i < _len):
            # 垂直添加
            for idx in xrange(0,numRows):
                if i < _len:
                    _map[idx].append(s[i])
                    i = i + 1
            # 对角线添加
            for idx in xrange(numRows - 2, 0, -1):
                if i < _len:
                    _map[idx].append(s[i])
                    i = i + 1

        return "".join(["".join(_map[x]) for x in xrange(numRows)])


def main():
    print Solution().convert('PAYPALISHIRING', 3)

if __name__ == '__main__':
    main()
