class Solution(object):
    def reverse(self, x):

        r = 0
        s = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            d = x % 10
            r = r * 10 + d
            x //= 10
        if r < -2**31 or r > 2**31 - 1:
            return 0
        
        return s * r