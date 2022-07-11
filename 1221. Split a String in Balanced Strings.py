class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c, rc, lc = 0, 0, 0
        for i in s:
            if i == 'R':
                rc += 1
            else:
                lc += 1
            if rc == lc:
                c += 1
                rc, lc = 0, 0
        return(c)
