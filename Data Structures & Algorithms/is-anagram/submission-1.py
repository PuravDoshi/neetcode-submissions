class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # n = len(s)
        # m = len(t)
        # if m != n:
        #     return False
        # self.s_hashmap = {}
        # self.t_hashmap = {}
        # for i in range(n):
        #     if s[i] not in self.s_hashmap:
        #         self.s_hashmap[s[i]] = 1
        #     else:
        #         self.s_hashmap[s[i]] = self.s_hashmap[s[i]] + 1
        # for i in range(m):
        #     if t[i] not in self.t_hashmap:
        #         self.t_hashmap[t[i]] = 1
        #     else:
        #         self.t_hashmap[t[i]] = self.t_hashmap[t[i]] + 1
        # for i in self.s_hashmap:
        #     if i not in self.t_hashmap:
        #         return False
        #     else:
        #         if self.s_hashmap[i] != self.t_hashmap[i]:
        #             return False
        # return True
        count_s = [0] * 26
        count_t = [0] * 26
        for i in s:
            count_s[ord(i) - 97] = count_s[ord(i) - 97] + 1
        for i in t:
            count_t[ord(i) - 97] = count_t[ord(i) - 97] + 1
        if count_s == count_t:
            return True
        else:
            return False