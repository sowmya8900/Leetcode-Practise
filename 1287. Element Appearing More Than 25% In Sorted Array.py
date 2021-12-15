class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        f = {}
        for i in arr:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        #print(f)
        tf = len(arr) * 0.25
        #print(tf)
        
        for k, v in f.items():
            if v > tf:
                return(k)
