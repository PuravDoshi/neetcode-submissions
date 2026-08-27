class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum():
                string = string + i
        string = string.lower()
        start = 0
        end = len(string) - 1
        flag = 0
        while(start <= end):
            if string[start] != string[end]:
                flag = 1
                break
            else:
                start = start + 1
                end = end - 1
        if flag == 1:
            return False
        else:
            return True