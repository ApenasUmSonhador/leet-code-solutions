class Solution(object):
    def isAnagram(self, s, t):
        original = dict()
        test = dict()
        for i in s:
            if i in original:
                original[i] += 1
            else:
                original[i] = 0
        for i in t:
            if i in test:
                test[i] += 1
            else:
                test[i] = 0
        return test == original