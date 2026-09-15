class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        n = len(s)
        l = 0
        for i in range(n):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] = count[s[i]] + 1
            max_freq = max(count.values())

            while (i - l + 1) - max_freq > k:
                count[s[l]] = count[s[l]] - 1
                l = l + 1
            max_length = max(max_length, ((i - l) + 1))
        return max_length