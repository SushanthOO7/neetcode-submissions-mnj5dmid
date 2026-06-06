class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if heights[i] > heights[j]:
                    d = heights[i] - heights[j]
                    v = (heights[i] - d) * (j - i)
                    if v > res:
                        res = v
                else:
                    d = heights[j] - heights[i]
                    v = (heights[j] - d) * (j - i)
                    if v > res:
                        res = v
        return res