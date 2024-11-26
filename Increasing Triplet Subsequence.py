class Solution(object):
    def increasingTriplet(self, nums):
        """
        Check if there exists an increasing triplet subsequence in nums.
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')  
        second = float('inf')

        for num in nums:
            if num <= first:  
                first = num
            elif num <= second: 
                second = num
            else:  the triplet
                return True
        
        return False
