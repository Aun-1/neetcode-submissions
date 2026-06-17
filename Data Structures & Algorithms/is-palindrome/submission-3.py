import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        str=''.join(chars)
        for i in range(len(str)//2):
            if str[i]!=str[len(str)-i-1]:
                return False
        return True
