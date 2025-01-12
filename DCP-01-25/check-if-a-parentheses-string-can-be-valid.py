class Solution(object):
    def canBeValid(self, s, locked):
        if len(s) % 2 != 0:
            return False
        o = c = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                o += 1
            else:
                o -= 1
            if o < 0:
                return False


        for i in range(len(s)-1,-1,-1):
            if locked[i] == '0' or s[i] == ')':
                c += 1
            else:
                c -= 1
            if c < 0:
                return False
        return True 
