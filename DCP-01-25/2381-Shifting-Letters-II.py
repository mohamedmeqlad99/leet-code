class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        shift_array = [0] * (n + 1)
        
        for l, r, d in shifts:
            if d == 1:
                shift_array[l] += 1
                if r + 1 < n:
                    shift_array[r + 1] -= 1
            else:
                shift_array[l] -= 1
                if r + 1 < n:
                    shift_array[r + 1] += 1
        
        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]
        
        result = []
        for i in range(n):
            shift = (shift_array[i] + 26) % 26
            result.append(chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a')))
        
        return ''.join(result)
