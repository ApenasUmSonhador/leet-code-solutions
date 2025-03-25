class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            i = (r - l) // 2 + l
            if nums[r] < nums[i]:
                l = i + 1
            else:
                r = i
        return nums[l]