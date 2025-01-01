class Solution(object):
    def maxScore(self, s):
        total_ones = s.count('1')
        running_zeros = 0
        best_score = 0
    
        for i in range(len(s) - 1):
            if s[i] == '0':
                running_zeros += 1
            else:
                total_ones -= 1
            current_score = running_zeros + total_ones
            best_score = max(best_score, current_score)
    
        return best_score