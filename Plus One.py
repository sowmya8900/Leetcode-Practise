class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sn = ''
        l = []
        for i in digits:
            sn += str(i)
        n = int(sn)
        po = str(n+1)
        for i in po:
            l.append(int(i))
        return(l)
        
