class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        f = {}
        
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        
        for i in range(len(s)):
            if s[i] not in f:
                f[s[i]] = t[i]
            else:
                if t[i] != f[s[i]]:
                    return False
        return True
