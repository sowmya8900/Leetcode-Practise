class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        f = {}
        l = []
        ans = -1
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        print(f)
        
        for k, v in f.items():
            if v == 1:
                ans = max(ans, k)
                
        return ans
