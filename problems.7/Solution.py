# coding: utf-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        _t = str(abs(x))
        r = cmp(x,0)
        result = int(_t[::-1])

        return r*result*(result < 2**31)
        

def main():
    print Solution().reverse(12345)

if __name__ == '__main__':
    main()
