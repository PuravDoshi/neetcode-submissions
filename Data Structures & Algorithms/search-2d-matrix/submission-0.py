class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        column = len(matrix[0])
        row = len(matrix)
        target_row = 0
        flag = 0
        for i in range(row):
            if target <= matrix[i][-1]:
                flag = 1
                target_row = i
                break
        if flag == 0:
            return False
        search = matrix[target_row]
        n = len(search)
        left = 0
        right = n-1
        mid = 0
        while left <= right:
            mid = (left + right)//2
            if target == search[mid]:
                return True
            elif target < search[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
