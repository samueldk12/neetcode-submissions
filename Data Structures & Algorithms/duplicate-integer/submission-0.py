class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aux = []
        for i in range(len(nums)):
            if nums[i] not in aux:
                aux.append(nums[i])
            else:
                return True
        return False