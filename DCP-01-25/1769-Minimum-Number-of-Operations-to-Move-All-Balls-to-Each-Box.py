class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        res = [0] * n
        balls, moves = 0, 0

        # Calculate left-to-right moves
        for i in range(n):
            res[i] += moves
            balls += int(boxes[i])
            moves += balls

        balls, moves = 0, 0

        # Calculate right-to-left moves
        for i in reversed(range(n)):
            res[i] += moves
            balls += int(boxes[i])
            moves += balls

        return res
