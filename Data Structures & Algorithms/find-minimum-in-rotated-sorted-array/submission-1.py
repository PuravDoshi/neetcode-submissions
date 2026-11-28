class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        mini = float("inf")
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                mini = min(mini, nums[mid])
                right = mid - 1
            else:
                mini = min(mini, nums[left])
                left = mid + 1
        return mini