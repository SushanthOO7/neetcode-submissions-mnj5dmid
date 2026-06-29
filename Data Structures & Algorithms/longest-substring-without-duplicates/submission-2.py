class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            s_c = set()
            for j in range(i, len(s)):
                if s[j] not in s_c:
                    s_c.add(s[j])
                else:
                    break
            res = max(res, len(s_c))
        return res