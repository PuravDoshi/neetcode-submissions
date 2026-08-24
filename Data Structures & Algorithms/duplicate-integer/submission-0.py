class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.hash_map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in self.hash_map:
                self.hash_map[nums[i]] = self.hash_map[nums[i]] + 1
            else:
                self.hash_map[nums[i]] = 1
        for i in range(n):
            if self.hash_map[nums[i]] > 1:
                return True
        return False