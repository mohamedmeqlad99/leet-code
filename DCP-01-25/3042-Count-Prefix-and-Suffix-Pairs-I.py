class Solution(object):
    def countPrefixSuffixPairs(self, words):
        count = 0

        def isPrefixAndSuffix(str1, str2):
            s1 = len(str1)
            s2 = len(str2)
            return str2[:s1] == str1 and str2[-s1:] == str1 and len(str2) >= len(str1) 

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count