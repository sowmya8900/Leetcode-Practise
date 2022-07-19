class Solution:
    def countPoints(self, rings: str) -> int:
        '''f = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        
        for i in range(1, len(rings), 2):
            if rings[i-1] == 'B' and f[int(rings[i])] == 0:
                f[int(rings[i])] += 1
        print(f)
        
        for i in range(1, len(rings), 2):
            if rings[i-1] == 'G' and f[int(rings[i])] != 0:
                f[int(rings[i])] += 1
        print(f)
        
        for i in range(1, len(rings), 2):
            if rings[i-1] == 'R' and f[int(rings[i])] != 0:
                f[int(rings[i])] += 1
        print(f)'''
        
        r = []
        b = []
        g = []
        
        for i in range(1, len(rings), 2):
            if rings[i-1] == 'R':
                r.append(int(rings[i]))
            if rings[i-1] == 'B':
                b.append(int(rings[i]))
            if rings[i-1] == 'G':
                g.append(int(rings[i]))
            
        print(r,b,g)
        s = list(set(r).intersection(set(b)))
        a = list(set(s).intersection(set(g)))
        return(len(a))
