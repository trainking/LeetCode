# coding: utf-8

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        result = None
        m = None
        for s in strs:
            if result == None:
                result = [c for c in s]
                m = [1 for c in s]
            elif len(result) > 0:
                for i,c in enumerate(s):
                    if i < len(result):
                        if result[i] != c:
                            if i == 0:
                                return ""
                            else:
                                m[i] = 0
                if len(s) < len(result):
                    result = result[0: len(s)]
                    m = m[0: len(s)]
        c = 0
        if result == None:
            return ""
        if len(m) > 0 and m[0] == 0:
            return ""
        for mi in m:
            if mi == 1:
                c += 1
            else:
                break
        return "".join(result[0:c])

def main():
    print Solution().longestCommonPrefix([])
    print Solution().longestCommonPrefix(["c","acc","ccc"])
    print Solution().longestCommonPrefix(["flower","flow","flight"])
    print Solution().longestCommonPrefix(["dog","racecar","car"])
    print Solution().longestCommonPrefix(["aac","acab","aa","abba","aa"])

if __name__ == '__main__':
    main()