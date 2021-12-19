class Solution:
    def isArmstrong(self, n: int) -> bool:
        l = len(str(n))
        s = 0
        for i in str(n):
            s += int(i) ** l
            #print(s)
        
        if s == n:
            return True
        return False
