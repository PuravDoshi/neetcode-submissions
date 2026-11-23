class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in hash_map:
                return [hash_map[diff], i]
            else:
                hash_map[nums[i]] = i