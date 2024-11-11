class Solution(object):
    def isValid(self, s):
        stack = []
        B = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in B:
                top = stack.pop() if stack else ''
                if B[c] != top:
                    return False
            else:
                stack.append(c)
        return not stack