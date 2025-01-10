class Solution(object):
    def wordSubsets(self, words1, words2):
        c = Counter()
        for w in words2:
            c |= Counter(w)
        return [i for i in words1 if c - Counter(i) == Counter() ]
        