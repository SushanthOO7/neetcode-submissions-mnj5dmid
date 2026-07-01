class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            key = tuple(sorted(word))
            d.setdefault(key, []).append(word)
        return list(d.values())