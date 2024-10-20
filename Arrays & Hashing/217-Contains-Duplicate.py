class Solution(object):
    def containsDuplicate(self, nums):
        n = set()
        for i in nums:
            if i in n:
                return True
            n.add(i)
        return False
        