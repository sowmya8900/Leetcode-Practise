class Solution:
    def isHappy(self, n: int) -> bool:
        l = []
        while(n != 1):
            s = str(n)
            x = 0
            for i in s:
                x += (int(i) ** 2)
            n = int(x)
            if n in l:
                return False
            else:
                l.append(n)
        return True
