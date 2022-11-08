class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t += " "
        flag = 1
        for i in s:
            if flag == 1:
                if i in t:
                    ind = t.index(i)
                    t = t[ind+1:]
                    flag = 1
                else:
                    flag = 0
            else:
                flag = 0
        if flag == 0:
            return False
        return True
