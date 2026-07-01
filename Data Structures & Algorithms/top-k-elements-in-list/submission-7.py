class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_c = {}
        l = [[] for i in range(len(nums) + 1)]

        for n in nums:
            n_c[n] = n_c.get(n, 0) + 1
        
        res = []

        for key,v in n_c.items():
            l[v].append(key)

        for i in reversed(l):
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res
