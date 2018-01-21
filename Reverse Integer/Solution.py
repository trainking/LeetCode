# coding: utf-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        _t = str(abs(x))
        result = 0
        if x < 0:
            result = -int(_t[::-1])
            if (result < -214783648):
                return 0
        elif x > 0:
            result = int(_t[::-1])
            if result > 2147483647:
                return 0

        return result
        

def main():
    print Solution().reverse(1534236469)

if __name__ == '__main__':
    main()
