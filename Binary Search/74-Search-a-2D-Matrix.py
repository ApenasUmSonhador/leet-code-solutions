class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line = self.findLineWithTarget(matrix,target)
        return self.binarySearch(line,target)

    def findLineWithTarget(self, matrix, target):
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                return matrix[i]
        return []

    def binarySearch(self, array, target):
        l, r = 0, len(array)-1
        while l <= r:
            i = (r - l)//2 + l
            if array[i] > target:
                r = i-1
            elif array[i] < target:
                l = i+1
            else:
                return True
        return False