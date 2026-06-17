class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        present_at = {}
        for i, num in enumerate(nums):
            if num in present_at:
                return True
            present_at[num] = i
        return False