class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        f = {}
        for i in arr1:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        #print(f)
        
        l = []
        
        for i in arr2:
            if i in arr1:
                l1 = [i] * f[i]
                
                l.extend(l1)
        l2 = []
        for i in arr1:
            if i not in arr2:
                
                l2.append(i)
        l.extend(sorted(l2))
        return(l)
