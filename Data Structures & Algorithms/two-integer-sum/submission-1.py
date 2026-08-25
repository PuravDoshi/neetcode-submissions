class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.hash_map = {}
        diff = 0
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in self.hash_map:
                return [self.hash_map[diff], i]
            else:
                self.hash_map[nums[i]] = i