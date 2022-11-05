class Solution:
    def romanToInt(self, s: str) -> int:
        f = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
        n = 0
        for i in range(0, len(s)-1):
            if list(f).index(s[i]) <= list(f).index(s[i+1]):
                n += f[s[i]]
                #print(n)
            else:
                n -= f[s[i]]
        n += f[s[-1]]
        return(n)
