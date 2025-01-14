class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        result = []
        for i in range(len(A)):
            result.append(len(set(A[:i + 1]) & set(B[:i + 1])))
        return result 
