class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            i = haystack.find(needle)
            return(i)
        else:
            return("-1")
        
