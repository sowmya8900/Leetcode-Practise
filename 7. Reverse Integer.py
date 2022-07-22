class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        r = s[::-1]
        if x == 0:
            return 0
        for i in r:
            if i == '0':
                r = r.replace(i, '', 1)
            else:
                break
        if(r[-1] == '-'):
            r = '-' + r[:-1]
        if int(r) > 2**31-1 or int(r) < -2**31:
            return 0
        else:
            return r
