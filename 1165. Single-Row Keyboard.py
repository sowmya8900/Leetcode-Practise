class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        c = 0
        curr = 0
        for i in word:
            ind = keyboard.find(i)
            d = abs(curr-ind)
            c += d
            curr = ind
        return(c)
