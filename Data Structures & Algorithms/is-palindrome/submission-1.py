import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=''
        for c in s:
            if c in string.ascii_letters or c in string.digits:
                str=str+c
        str=str.lower()
        for i in range(len(str)//2):
            if str[i]!=str[len(str)-i-1]:
                return False
        return True
