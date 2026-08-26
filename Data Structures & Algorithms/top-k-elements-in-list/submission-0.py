class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        self.hash_map = {}
        for i in range(n):
            if nums[i] not in self.hash_map:
                self.hash_map[nums[i]] = 1
            else:
                self.hash_map[nums[i]] = self.hash_map[nums[i]] + 1
        sort = dict(sorted(self.hash_map.items(), key=lambda item: item[1], reverse=True))
        a = list(sort.keys())[0:k]
        return a

