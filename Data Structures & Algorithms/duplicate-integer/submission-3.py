class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s_nums = sorted(nums)
        for i in range(len(s_nums) - 1):
            if s_nums[i] == s_nums[i + 1]:
                return True
        return False