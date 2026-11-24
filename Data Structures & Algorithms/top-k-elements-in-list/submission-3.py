class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        n = len(nums)
        for i in range(n+1):
            freq.append([])
        hash_map = {}
        for i in range(n):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] = hash_map[nums[i]] + 1
        for key, val in hash_map.items():
            freq[val].append(key)
        
        final = []
        count = 0
        for i in range(n, -1, -1):
            for j in freq[i]:
                final.append(j)
                count = count + 1
                if count == k:
                    return final