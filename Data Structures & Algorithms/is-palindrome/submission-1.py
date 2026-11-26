class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ""
        n = len(s)
        for i in range(n):
            if (s[i] >= "a" and s[i] <= "z") or (s[i] >= "0" and s[i] <= "9"):
                temp = temp + s[i]
        m = len(temp)
        left = 0
        right = m - 1
        while left <= right:
            if temp[left] != temp[right]:
                return False
            left = left + 1
            right = right - 1
        return True