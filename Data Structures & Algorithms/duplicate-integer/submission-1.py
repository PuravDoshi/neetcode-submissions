class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] = hash_map[nums[i]] + 1
        for i in range(n):
            if hash_map[nums[i]] > 1:
                return True
        return False