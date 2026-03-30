class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        e = []
        for i in strs:
            word = ""
            for j in i:
                c = ord(j) + 3
                word += chr(c)
            e.append(word)
        return '0'.join(e)

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        l = s.split("0")
        e = []
        for i in l:
            word = ""
            for j in i:
                c = ord(j) - 3
                word += chr(c)
            e.append(word)
        return e
