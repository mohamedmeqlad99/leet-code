from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0

        visited = set()
        queue = deque([(amount, 0)]) 

        while queue:
            remain, count = queue.popleft()

            if remain == 0:
                return count

            for coin in coins:
                new_remain = remain - coin
                if new_remain >= 0 and new_remain not in visited:
                    visited.add(new_remain)
                    queue.append((new_remain, count + 1))

        return -1
