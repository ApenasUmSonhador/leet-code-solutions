class Solution(object):
    def trap(self, height):
        a, n = 0, len(height)
        ml, mr = [0] * n, [0] * n
        ml[0], mr[n-1] = height[0], height[n-1]
        for i in range(1, n):
            ml[i] = max(height[i], ml[i-1])
            mr[n-i-1] = max(height[n-i-1], mr[n-i-2])
        for i in range(n):
            a += min(ml[i], mr[i]) - height[i]
        return a