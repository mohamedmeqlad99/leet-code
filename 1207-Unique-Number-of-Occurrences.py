class Solution:
    def uniqueOccurrences(self, arr):
        dic = {}
        
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        if len(set(dic.values())) != len(set(arr)):
            return False
        return True