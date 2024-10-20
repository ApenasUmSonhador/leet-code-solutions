class Solution(object):
    def threeSum(self, nums):
        l, m, r, ans = 0, 1, len(nums)-1, set()
        nums.sort()
        while l < len(nums)-2:
            while m < r:
                if nums[l] + nums[m] + nums[r] == 0:
                    ans.add((nums[l], nums[m], nums[r]))
                    m += 1
                while m < r and nums[l] + nums[m] + nums[r] < 0:
                    m += 1
                while m < r and nums[l] + nums[m] + nums[r] > 0:
                    r -= 1
            l += 1
            while[l] == nums[l-1]:
                l += 1
            m, r = l+1, len(nums)-1
        return [list(x) for x in ans]