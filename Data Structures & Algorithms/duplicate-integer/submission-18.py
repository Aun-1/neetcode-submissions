class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #random 
        return len(set(nums))<len(nums)