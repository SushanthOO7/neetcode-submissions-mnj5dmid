class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        dd = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            if t[i] in dd:
                dd[t[i]] += 1
            else:
                dd[t[i]] = 1
        return d == dd