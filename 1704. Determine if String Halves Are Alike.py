class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = [s[:len(s)//2], s[len(s)//2:]]
        cl, cr = 0, 0
        for i in range(0, len(l[0])):
            #print(l[0][i], l[1][i])
            if l[0][i] in "aeiouAEIOU":
                cl += 1
            if l[1][i] in "aeiouAEIOU":
                cr += 1
            #print(cl, cr)
        return cl == cr
