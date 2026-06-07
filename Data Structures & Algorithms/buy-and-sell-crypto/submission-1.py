class Solution:
    def maxProfit(self, a: List[int]) -> int:
        p = 0
        for i, v in enumerate(a[:-1]):
            for j in range(i + 1, len(a)):
                if v > a[j]:
                    continue
                else:
                    s = (v - a[j]) * -1
                    p = max(s, p)
        return  p