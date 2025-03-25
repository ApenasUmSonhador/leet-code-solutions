class Solution:
    def search(self, nums, target):

        pivot = self.findMinIndex(nums)

        l, r = 0, len(nums) - 1
        while l <= r:
            i = (r - l) // 2 + l
            mi = (i + pivot) % len(nums)
            if nums[mi] > target:
                r = i - 1
            elif nums[mi] < target:
                l = i + 1
            else:
                return mi
        return -1

    def findMinIndex(self, nums):
        # Problem 143-Find Minimum in Rotated Sorted Array
        l, r = 0, len(nums) - 1
        while l < r:
            i = (r - l) // 2 + l
            if nums[r] < nums[i]:
                l = i + 1
            else:
                r = i
        return l
