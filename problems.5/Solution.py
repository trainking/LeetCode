# coding: utf-8
# use python 2.7

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        for i in range(0, len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            _max = max(len1, len2)
            if _max > end - start:
                start = i - (_max - 1) / 2
                end = i + _max / 2

        return s[start : end + 1]


    def expandAroundCenter(self, s, left, right):
        L, R = left, right
        while(L >= 0 and R < len(s) and s[L] == s[R]):
            L -= 1
            R += 1
        return R - L - 1


def main():
    print Solution().longestPalindrome("babad")

if __name__ == '__main__':
    main()
