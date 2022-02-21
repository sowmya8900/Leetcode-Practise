class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l = []
        
        for i in words:
            s = ""
            for c in i:
                s += alp[ord(c) - 97]
            if s not in l:
                l.append(s)
        return(len(l))
