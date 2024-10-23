class Solution(object):
    def missingNumber(self, nums):
        S = ((len(nums)+1)* (len(nums)))/2
        s = 0
        for x in nums:
            s += x
        return S - s
        