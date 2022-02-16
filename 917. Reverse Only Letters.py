class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = []
        for i in s:
            if i.isalpha():
                l.append(i)
        #l.reverse()
        #print(l)
        for i in range(len(s)):
            if s[i].isalpha():
                #s = s.replace(s[i], l[-1], 1)
                s = s[:i] + l[-1] + s[i+1:]
                #print(s)
                del (l[-1])
        return(s)
