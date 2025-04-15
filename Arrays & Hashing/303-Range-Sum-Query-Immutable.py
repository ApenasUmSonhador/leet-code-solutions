class NumArray:
    l=[]
    def __init__(self, nums: List[int]):
        self.l = [nums[0]]
        for i in range(1, len(nums)):
            self.l.append(nums[i] + self.l[i-1])

    def sumRange(self, left: int, right: int) -> int:
        if left <= 0:
            return self.l[right]
        return self.l[right] - self.l[left-1]
