from collections import Counter
import math
class Solution(object):
    def numRabbits(self, answers):
        c = Counter(answers)
        total = 0
        for n, f in c.items():
            group_size = n + 1
            groups = math.ceil(f / float(group_size))
            total += groups * group_size
        return int(total)