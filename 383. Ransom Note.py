class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = []
        for i in ransomNote:
            if (i not in l) and (ransomNote.count(i) > magazine.count(i)):
                return False
            l.append(i)
        return True
