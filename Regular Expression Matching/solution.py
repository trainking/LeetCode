# coding: utf-8

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_l = len(s)
        p_l = len(p)
        y = 0
        c = 0
        n = 0
        v = ""
        d = ""
        while n < p_l:
            if (n + 1) < p_l and p[n + 1] == "*":
                while y < s_l and (p[n] == s[y] or p[n] == "."):
                    v = p[n]
                    d = s[y]
                    y +=1
                    c +=1
                n = n + 2
            else:
                if d == p[n] or p[n] == ".":
                    n = n + 1
                    continue
                if y < s_l:
                    if (p[n] == s[y] or p[n] == "."):
                        y +=1
                        c +=1
                        n = n + 1
                    else:
                        if v == p[n] or p[n]==".":
                            n += 1
                        else:
                            return False
                else:
                    n = n + 1
                    c += 1
        return c == s_l
                
                

                



def main():
    obj = Solution()
    # 测试用例
    # assert obj.isMatch("aa", "a") == False
    # assert obj.isMatch("aa", "a*") == True
    # assert obj.isMatch("ab", ".*") == True
    # assert obj.isMatch("aab", "c*a*b") == True
    # assert obj.isMatch("mississippi", "mis*is*p*.") == False
    # assert obj.isMatch("ab", ".*c") == False
    # assert obj.isMatch("aaa", "a*a") == True
    # assert obj.isMatch("aaa", "aaaa") == False
    # assert obj.isMatch("aaa", "ab*a") == False
    # assert obj.isMatch("aaa", "ab*ac*a") == True
    # assert obj.isMatch("aaa", "ab*a*c*a") == True
    # assert obj.isMatch("bbbba", ".*a*a") == True
    # assert obj.isMatch("ab", ".*..") == True
    assert obj.isMatch("a", ".*..a*") == False

if __name__ == '__main__':
    main()