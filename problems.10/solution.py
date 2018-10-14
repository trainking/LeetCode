# coding: utf-8

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        first = bool(s) and p[0] in (s[0], ".")

        if len(p) >= 2 and p[1] == "*":
            return (self.isMatch(s, p[2:])) or (first and self.isMatch(s[1:], p))
        else:
            return first and self.isMatch(s[1:], p[1:])
                
                



def main():
    obj = Solution()
    # 测试用例
    assert obj.isMatch("aa", "a") == False
    assert obj.isMatch("aa", "a*") == True
    assert obj.isMatch("ab", ".*") == True
    assert obj.isMatch("aab", "c*a*b") == True
    assert obj.isMatch("mississippi", "mis*is*p*.") == False
    assert obj.isMatch("ab", ".*c") == False
    assert obj.isMatch("aaa", "a*a") == True
    assert obj.isMatch("aaa", "aaaa") == False
    assert obj.isMatch("aaa", "ab*a") == False
    assert obj.isMatch("aaa", "ab*ac*a") == True
    assert obj.isMatch("aaa", "ab*a*c*a") == True
    assert obj.isMatch("bbbba", ".*a*a") == True
    assert obj.isMatch("ab", ".*..") == True
    assert obj.isMatch("a", ".*..a*") == False

if __name__ == '__main__':
    main()