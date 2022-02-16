class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #flag = 1
        temp = s
        if s == goal:
            return True
        s = s[1:] + s[0]
        while(s != temp):
            if s == goal:
                return True
            s = s[1:] + s[0]
        return False
