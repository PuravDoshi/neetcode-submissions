class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(numbers)
        difference = 0
        for i in range(n):
            difference = target - numbers[i]
            if difference in hash_map:
                return [hash_map[difference]+1, i+1]
            hash_map[numbers[i]] = i
