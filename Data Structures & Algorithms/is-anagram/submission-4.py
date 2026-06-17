class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # random 
        return sorted(s)==sorted(t)