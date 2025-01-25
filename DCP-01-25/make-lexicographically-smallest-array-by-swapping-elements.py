class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        groups = []
        num_groups = {}
        for i in sorted(nums):
            if not groups or abs(i - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(i)
            num_groups[i] = len(groups) - 1
        res = []
        for i in nums:
            j = num_groups[i]
            res.append(groups[j].popleft())
        return res
