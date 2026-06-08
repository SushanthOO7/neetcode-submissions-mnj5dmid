class Solution:
    def isValid(self, s: str) -> bool:
        p = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        a = []
        for i in s:
            if i in p:
                if a and a[-1] == p[i]:
                    a.pop()
                else:
                    return False
            else:
                a.append(i)
        return not a
