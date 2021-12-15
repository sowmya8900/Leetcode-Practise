class Solution:
    def findComplement(self, num: int) -> int:
        b = format(num, "b")
        c = ''
        
        for i in b:
            if i == '0':
                c += '1'
            elif i == '1':
                c += '0'
        
        ans = int(c, 2)
        return(ans)
        
