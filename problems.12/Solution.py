# coding: utf-8

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        r = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result = []
        i  = 0
        while i < len(m):
            t = num - m[i]
            if t > 0 :
                result.append(r[i])
                num = t
            elif t == 0:
                result.append(r[i])
                return "".join(result)
            else:
                i += 1 

def main():
    print  Solution().intToRoman(3)   # output: "III"
    print  Solution().intToRoman(4)   # output: "IV" 
    print  Solution().intToRoman(9)   # output: "IX"
    print  Solution().intToRoman(58)  # output: "LVIII"
    print  Solution().intToRoman(1994) # output: "MCMXCIV"


if __name__ == '__main__':
    main()