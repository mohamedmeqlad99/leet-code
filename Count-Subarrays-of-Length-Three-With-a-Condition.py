class Solution(object):
    def countSubarrays(self, nums):
        c = 0
        for i in range(1,len(nums) -1):
            if nums[i] / 2.0 == nums[i-1] + nums[i+1]:
                c = c + 1
        return c