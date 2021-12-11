class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = list(sentence.split())
        #print(l)
        
        for w in l:
            if (w.find(searchWord) == 0):
                return(l.index(w)+1)
        return -1
        
