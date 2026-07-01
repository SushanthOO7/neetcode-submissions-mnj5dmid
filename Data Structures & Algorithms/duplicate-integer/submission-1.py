class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = []
        for i in nums:
            if i in n:
                return True
            else:
                n.append(i)
        return False