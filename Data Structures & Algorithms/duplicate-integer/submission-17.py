class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #random 
        if len(set(nums))<len(nums):
            return True
        return False