class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = {}
        difference = 0
        for i in range(n):
            difference = target - nums[i]
            if difference in hash_map:
                return [hash_map[difference], i]
            else:
                hash_map[nums[i]] = i