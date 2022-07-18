import collections
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        l = []
        c = 0
        n = 0
        f = collections.Counter(nums)
        print(f)
        
        for k,v in f.items():
            if v == 2:
                c += 1
            elif v < 2:
                n += 1
            elif v > 2:
                n += v%2
                c += (v//2)
                
                
        l.append(c)
        l.append(n)
        

        return(l)
