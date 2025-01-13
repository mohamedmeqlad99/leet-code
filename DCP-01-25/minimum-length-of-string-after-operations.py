from collections import Counter
class Solution(object):
    def minimumLength(self, s):
        c = Counter(s)
        minus = 0
        for x in c.values():
            while x >= 3:
                x -= 2
                minus += 2
        return len(s) - minus
