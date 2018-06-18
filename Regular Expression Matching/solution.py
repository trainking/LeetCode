# coding: utf-8

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """



def main():
    obj = Solution()
    # 测试用例
    assert obj.isMatch("aa", "a") == False
    assert obj.isMatch("aa", "a*") == True
    assert obj.isMatch("ab", ".*") == True
    assert obj.isMatch("aab", "c*a*b") == True
    assert obj.isMatch("mississippi", "mis*is*p*.") == False

if __name__ == '__main__':
    main()