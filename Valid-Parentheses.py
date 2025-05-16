class Solution(object):
    def isValid(self,s):
           stack = []
           bracket_map = {')': '(', '}': '{', ']': '['}
           for c in s:
            if c in bracket_map:
                top = stack.pop() if stack else '#'
                if bracket_map[c] != top:
                    return False
            else:
                stack.append(c)
           return not stack

