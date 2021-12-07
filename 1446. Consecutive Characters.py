class Solution:
    def maxPower(self, s: str) -> int:
        c = 1
        maxc = 1
        for i in range(0, len(s)-1):
            if(s[i] == s[i+1]):
                c += 1
                maxc = max(maxc, c)
            
            else:
                c = 1
        return(maxc)
            
