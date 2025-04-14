class Solution(object):
    def countGoodTriplets(self, nums, x, y, z):
        res = 0
        length = len(nums)
        i = 0
        while i < length:
            j = i + 1
            while j < length:
                if abs(nums[i] - nums[j]) <= x:
                    k = j + 1
                    while k < length:
                        if abs(nums[j] - nums[k]) <= y and abs(nums[i] - nums[k]) <= z:
                            res += 1
                        k += 1
                j += 1
            i += 1
        return res
