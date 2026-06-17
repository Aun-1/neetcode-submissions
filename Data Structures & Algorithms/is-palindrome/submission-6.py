import string
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # str=''
        # for c in s:
        #     if c in string.ascii_letters or c in string.digits:
        #         str=str+c #this ass hole line makes TC O(n)
        # str=str.lower()

        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        str=''.join(chars)
        for i in range(len(str)//2):
            if str[i]!=str[len(str)-i-1]:
                return False
        return True

