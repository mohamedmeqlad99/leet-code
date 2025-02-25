class Solution:
    def numOfSubarrays(self, arr):
        res, even, odd, mod = 0, 0, 0, 10**9 + 7

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] % 2 == 1: 
                even, odd = odd, (even + 1) % mod
            else:  
                even = (even + 1) % mod
            
            res = (res + odd) % mod
        
        return res
