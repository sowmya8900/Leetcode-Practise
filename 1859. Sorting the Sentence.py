class Solution:
    def sortSentence(self, s: str) -> str:
        l = list(s.split())
        #print(l)
        s1 = ""

        l.sort(key=lambda x:int(x[-1]))
        for i in l[:-1]:
            s1 += i[:-1] + " "
        s1 += l[-1][:-1]
        return(s1)
