class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # TC of O(n)
        seen_variable = set()
        for num in nums:
            if num in seen_variable: 
                return True
            seen_variable.add(num)
        return False