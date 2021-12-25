class Solution:
    def confusingNumber(self, n: int) -> bool:
        pairs = {0:0, 1:1, 6:9, 8:8, 9:6}
        ans = False
        s = ''
        for i in str(n):
            #print(i)
            if int(i) in pairs.keys():
                #print(i)
                s += str(pairs[int(i)])
                ans = True
            else:
                return False
        print(s)
        if int(s[::-1]) == n:
            return False
        else:
            return ans
