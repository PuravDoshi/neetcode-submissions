class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        s_array = [0] * 26
        t_array = [0] * 26
        for i in range(m):
            s_array[ord(s[i]) - 97] = s_array[ord(s[i]) - 97] + 1
        for i in range(n):
            t_array[ord(t[i]) - 97] = t_array[ord(t[i]) - 97] + 1
        if s_array == t_array:
            return True
        else:
            return False