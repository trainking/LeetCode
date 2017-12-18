# coding: utf-8
# use python 2.7

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        _max = 0
        _mas = {}
        j = 0 
        for i in range(len(s)):
            if _mas.has_key(s[i]) and j <= _mas[s[i]]:
                j = max(j, _mas[s[i]] + 1)
            else:
                _max = max(_max, i - j + 1)
            _mas[s[i]] = i

        return _max

def main():
    print Solution().lengthOfLongestSubstring("abcabcbb")

if __name__ == '__main__':
    main() 
