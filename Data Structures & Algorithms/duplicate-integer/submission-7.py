class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set(nums) makes a set and automatically removes duplicates
        return len(set(nums))<len(nums)

        