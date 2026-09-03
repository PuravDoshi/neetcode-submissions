class Solution:
    def encode(self, strs: List[str]) -> str:
        sep = "#"
        encoded_string = ""
        for i in strs:
            encoded_string = encoded_string + str(len(i)) + sep + i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res