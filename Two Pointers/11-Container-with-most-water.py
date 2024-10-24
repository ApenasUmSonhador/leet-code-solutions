class Solution:
    def maxArea(self, height: List[int]) -> int:
        s, l, r = 0, 0, len(height)-1
        while l < r:
            new_s = (r-l) * min(height[l], height[r])
            if new_s > s:
                s = new_s
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return s