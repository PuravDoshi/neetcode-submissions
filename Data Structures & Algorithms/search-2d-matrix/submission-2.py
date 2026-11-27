class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l_out = 0
        r_out = row - 1
        mid_out = 0
        while l_out <= r_out:
            mid_out = (l_out + r_out) // 2
            if (target >= matrix[mid_out][0]) and (target <= matrix[mid_out][col-1]):
                temp = matrix[mid_out]
                left = 0
                right = col - 1
                mid = 0
                while left <= right:
                    mid = (left + right) // 2
                    if temp[mid] == target:
                        return True
                    elif temp[mid] < target:
                        left = left + 1
                    else:
                        right = right - 1
                return False
            elif matrix[mid_out][0] < target:
                l_out = l_out + 1
            else:
                r_out = r_out - 1
        return False