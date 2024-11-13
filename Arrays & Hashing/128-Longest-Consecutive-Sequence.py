class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        bigger = 0
        for x in nums:
            if x-1 not in num_set:
                aux = 1
                while x + aux in num_set:
                    aux += 1
                bigger = max(bigger, aux)
        return bigger