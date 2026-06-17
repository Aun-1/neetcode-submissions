class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False
       
        arr=[0]*26


        for i in range(len(s)):
            arr[ord(s[i])-ord('a')]+=1
            arr[ord(t[i])-ord('a')]-=1
       
        for val in arr:
            if val!=0:
                return False
        return True

#the soltuion above is better bcz SC [O]*26 is O(1) where in dict it is O(n)
        # if len(s)!=len(t):
        #     return False
        
        # dict_s={}

        # for c in s:
        #     dict_s[c]=dict_s.get(c,0)+1
        
        # for c in t:
        #     dict_s[c]=dict_s.get(c,0)-1
        
        # for c in dict_s:
        #     if dict_s[c]!=0:
        #         return False
        # return True



