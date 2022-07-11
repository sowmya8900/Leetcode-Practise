class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = []
        if n == 1:
            return [0]
        i = 1
        while(i < n):
            l.extend([i, -1*(i)])
            i += 2
        if n%2 != 0:
            l.append(0)
        return(l)
