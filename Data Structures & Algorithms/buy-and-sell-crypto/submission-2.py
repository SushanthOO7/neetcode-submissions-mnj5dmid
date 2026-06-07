class Solution:
    def maxProfit(self, a: List[int]) -> int:
        l, r = 0, 1
        max_p = 0
        while r < len(a):
            if a[l] < a[r]:
                p = a[r] - a[l]
                max_p = max(max_p, p)
            else:
                l = r
            r += 1
        return max_p