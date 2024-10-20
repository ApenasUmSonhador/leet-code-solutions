# Even unintentionally, this code has a runtime of 0.0ms.
# Even though it doesn't look extraordinary.
class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [num_dict[diff], i]
            num_dict[num] = i
        return None