class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l <= r:
            while l < r and not self.isAlnum(s[l]):
                l += 1
            while r > l and not self.isAlnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True
        
    def isAlnum(self, a):
        return (ord('A') <= ord(a) <= ord('Z') or
                ord('a') <= ord(a) <= ord('z') or
                ord('0') <= ord(a) <= ord('9'))