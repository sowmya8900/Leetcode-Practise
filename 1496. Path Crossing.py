class Solution:
    def isPathCrossing(self, path: str) -> bool:
        p = [0,0]
        l = [[0,0]]
        for i in path:
            if i == 'N':
                p[1] += 1
            
            elif i == 'E':
                p[0] += 1
            
            elif i == 'W':
                p[0] -= 1
            
            elif i == 'S':
                p[1] -= 1
            
            print(p)
            a = p[:]
            if a not in l:
                l.append(a)
                print(l)
            else:
                return True
            
        return False
