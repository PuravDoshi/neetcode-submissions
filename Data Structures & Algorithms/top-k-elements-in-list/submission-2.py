class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hash_map = {}
        n = len(nums)
        for i in range(n + 1):
            result.append([])
        for i in range(n):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] = hash_map[nums[i]] + 1
        for num, freq in hash_map.items():
            result[freq].append(num)
        count = 0
        final_result = []
        for i in range(len(result)-1, -1, -1):
            for j in result[i]:
                final_result.append(j)
                count = count + 1
                if count == k:
                    return final_result
            