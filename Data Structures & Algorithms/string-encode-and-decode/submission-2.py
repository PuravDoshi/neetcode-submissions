class Solution:
    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            final = final + str(len(i)) + "#" + i
        return final
    
    def decode(self, s: str) -> List[str]:
        final = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            temp = ""
            while s[j] != "#":
                temp = temp + s[j]
                j = j + 1
            length = int(temp)
            word = s[j+1: j+1+length]
            final.append(word)
            i = j + 1 + length
        return final
