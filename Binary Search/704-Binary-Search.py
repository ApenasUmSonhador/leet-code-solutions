class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (r - l) // 2 + l
            if nums[i] > target:
                r = i - 1
            elif nums[i] < target:
                l = i + 1
            else:
                return i
        return -1
