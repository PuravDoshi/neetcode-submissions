class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        flag = 0
        mid = 0
        while left <= right:
            if nums[left] == target:
                flag = 1
                return left
            if nums[right] == target:
                flag = 1
                return right
            mid = (left + right)//2
            if target == nums[mid]:
                flag = 1
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if flag == 0:
            return -1