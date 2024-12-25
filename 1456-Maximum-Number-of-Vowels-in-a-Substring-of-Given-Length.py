class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        m_v = 0
        c_v = 0
        
        for i in range(len(s)):
            if s[i] in vowels:
                c_v += 1
            if i >= k:
                if s[i - k] in vowels:
                    c_v -= 1
            m_v = max(c_v,m_v)

        
        return m_v
