class Solution:
    def frequencySort(self, s: str) -> str:
        s1 = ""
        f = {}
        
        for i in s:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        print(f)
        
        f1 = dict(sorted(f.items(), key=lambda item: item[1], reverse=True))
        print(f1)
        
        for k, v in f1.items():
            s1 += k*v
        return(s1)
            
        #print(''.join(f1))
