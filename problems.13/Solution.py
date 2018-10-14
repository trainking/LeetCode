# coding: utf-8

class Solution(object):
    def intToRoman(self, s):
        """
        :type num: int
        :rtype: str
        """
        m = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        r = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result = 0
        i = 0
        while i < len(s): 
            if s[i: i + 2] in r:
                index = r.index(s[i: i + 2])
                result += m[index]
                i += 2
            else:
                index = r.index(s[i])
                result += m[index]
                i += 1
        return result

def main():
    print  Solution().intToRoman("III")   # output: "3"
    print  Solution().intToRoman("IV")   # output: "4" 
    print  Solution().intToRoman("IX")   # output: "9"
    print  Solution().intToRoman("LVIII")  # output: "58"
    print  Solution().intToRoman("MCMXCIV") # output: "1994"


if __name__ == '__main__':
    main()