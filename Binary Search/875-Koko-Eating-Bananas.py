import math


class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        while l < r:
            v = (r - l) // 2 + l
            t = self.timeBySpeed(piles, v)
            if t > h:
                l = v + 1
            else:
                r = v
        return l

    def timeBySpeed(self, piles, v):
        t = 0
        for x in piles:
            t += math.ceil(x / v)
        return t
