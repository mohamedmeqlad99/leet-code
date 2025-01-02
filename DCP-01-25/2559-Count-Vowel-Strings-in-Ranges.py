class Solution(object):
    def vowelStrings(self, words, queries):
        def is_vowel(c):
            return c in {'a', 'e', 'i', 'o', 'u'}
        
        n = len(words)

        prefix = [0] * n
        for i, w in enumerate(words):
            if is_vowel(w[0]) and is_vowel(w[-1]): 
                prefix[i] = 1
        
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        
        result = []
        for l, r in queries:
            if l == 0:
                result.append(prefix[r])
            else:
                result.append(prefix[r] - prefix[l - 1])
        
        return result
