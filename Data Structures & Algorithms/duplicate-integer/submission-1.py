class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aux = set(nums)
        if len(aux) != len(nums):
            return True
        else:
            return False