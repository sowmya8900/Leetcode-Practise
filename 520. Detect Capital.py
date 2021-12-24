class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(all(x.isupper() for x in word)):
            return True
        elif(all(x.islower() for x in word)):
            return True
        else:
            if word[0].isupper():
                if(all(x.islower() for x in word[1:])):
                    return True
            else:
                return False
