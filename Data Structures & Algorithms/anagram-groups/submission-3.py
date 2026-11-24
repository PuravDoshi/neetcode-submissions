class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            temp = [0] * 26
            for i in s:
                temp[ord(i) - 97] = temp[ord(i) - 97] + 1
            result[tuple(temp)].append(s)
        final = list(result.values())
        return final