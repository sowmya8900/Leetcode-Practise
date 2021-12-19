class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ln, dn = [], []
        
        for i in emails:
            ln.append(i.split('@')[0])
            dn.append(i.split('@')[1])
        
        for l in range(len(ln)):
            if '.' in ln[l]:
                ln[l] = ln[l].replace('.','')
            
            if '+' in ln[l]:
                ln[l] = ln[l][: ln[l].find('+')]
        
        l = [(ln[i]+ '@' + dn[i]) for i in range(len(ln))]
        #print(l)
        l = set(l)
        c = len(l)
        return c
