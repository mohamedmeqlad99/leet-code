class Solution(object):
    def stringMatching(self, words):
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    if words[i] not in res:
                     res.append(words[i])
                   
        return res

        