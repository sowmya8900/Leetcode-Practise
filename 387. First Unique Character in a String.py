class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = {}
        for i in s:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        #print(f)
        for k,v in f.items():
            if v == 1:
                return s.find(k)
            
        return -1
