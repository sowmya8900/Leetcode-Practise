class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = list(s.split(' '))
        f = {}
        
        if len(pattern) != len(n) or len(set(n)) != len(set(pattern)):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in f:
                f[pattern[i]] = n[i]
            else:
                if n[i] != f[pattern[i]]:
                    return False
        return True
