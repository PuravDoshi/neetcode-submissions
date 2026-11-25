class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 1
        right = 1
        left_arr = [0] * n
        right_arr = [0] * n
        for i in range(n):
            left_arr[i] = left
            left = left * nums[i]
        for i in range(n-1, -1, -1):
            right_arr[i] = right
            right = right * nums[i]
        for i in range(n):
            nums[i] = left_arr[i] * right_arr[i]
        return nums
