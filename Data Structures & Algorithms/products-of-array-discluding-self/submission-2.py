class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        z = 0

        for i in nums:
            if i:
                p *= i
            else:
                z += 1
        
        if z > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, n in enumerate(nums):
            if z:
                if n:
                    res[i] = 0
                else:
                    res[i] = p
            else:
                res[i] = p//n
        
        return res