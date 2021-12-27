class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        l = list(sentence.split())
        for i in range(len(l)):
            a = 'a'*(l.index(l[i])+1)
            if l[i][0].lower() in ['a', 'e', 'i', 'o', 'u']:
                l[i] = l[i] +'ma' + a
            else:
                f = l[i][0]
                l[i] = l[i].replace(f, '', 1)
                l[i] = l[i] + f + 'ma' + a
                
        return ' '.join(l)
