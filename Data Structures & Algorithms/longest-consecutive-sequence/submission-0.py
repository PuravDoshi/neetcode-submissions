class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set()
        for i in nums:
            a.add(i)
        max_seq = 0
        count = 0
        x = 0
        for i in nums:
            if (i-1) in a:
                continue
            count = count + 1
            x = i
            while (x + 1) in a:
                count = count + 1
                x = x + 1
            max_seq = max(max_seq, count)
            count = 0
        return max_seq

            