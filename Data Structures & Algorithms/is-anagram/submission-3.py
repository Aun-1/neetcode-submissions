class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26 # array of length 26 since 26 aphalbets
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1

        for val in count:
            if val!=0:
                return False
        return True 

        