class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_length = 0
        n = len(s)
        for r in range(n):
            while s[r] in char_set:
                char_set.remove(s[l])
                l = l + 1
            char_set.add(s[r])
            max_length = max(max_length, (r - l) + 1)
        return max_length