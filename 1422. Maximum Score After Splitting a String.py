class Solution:
    def maxScore(self, s: str) -> int:
        l = []
        for i in range(1, len(s)):
            l.append(s[0:i].count('0')+s[i:].count('1'))
        return max(l)
        
