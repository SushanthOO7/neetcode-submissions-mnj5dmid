class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r = 0
        for i in nums:
            s = 0
            c = i
            while c in nums:
                c += 1
                s += 1
            r = max(r, s)
        return r