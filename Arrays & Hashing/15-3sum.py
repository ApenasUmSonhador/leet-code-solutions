class Solution(object):
    def threeSum(self, nums):
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                # because we have already checked the previous number
                continue
            self.twoSum(nums, i, ans)
        return [list(triplet) for triplet in ans]

    def twoSum(self, nums, i, ans):
        num_dict = {}
        target = -nums[i]
        for j in range(i+1, len(nums)):
            diff = target - nums[j]
            if diff in num_dict:
                ans.add((nums[i], diff, nums[j]))
            num_dict[nums[j]] = j