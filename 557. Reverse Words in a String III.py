class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split())
        print(l)
        s = ' '.join(x[::-1] for x in l)
        return(s)
