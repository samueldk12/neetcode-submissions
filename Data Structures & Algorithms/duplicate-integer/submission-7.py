class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            aux = {}
            for i in nums:
                if i not in aux:
                    aux[i] = True
                else:
                    return True
            return False