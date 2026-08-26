class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        self.hash_map = {}
        freq = []
        result = []
        for i in range(0,n+1):
            freq.append([])
        for i in range(n):
            if nums[i] not in self.hash_map:
                self.hash_map[nums[i]] = 1
            else:
                self.hash_map[nums[i]] = self.hash_map[nums[i]] + 1
        for key, val in self.hash_map.items():
            freq[val].append(key)
        for i in range(n, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
