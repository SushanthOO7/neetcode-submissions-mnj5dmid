class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        s_l = sorted(d.items(), key=lambda item : item[1])
        print(s_l)
        s_d = dict(s_l)
        res = []
        for key, value in reversed(s_d.items()):
            if k == 0:
                break
            else:
                res.append(key)
                k -= 1
        return res
