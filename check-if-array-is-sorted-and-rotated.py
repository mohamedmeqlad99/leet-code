class Solution(object):
    def check(self, nums):
        n=len(nums)
        s=sorted(nums)
        for i in range(n):
            if nums[i:]+nums[:i]==s:
                return True
            
        return False  
