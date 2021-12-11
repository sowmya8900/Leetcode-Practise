class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f = {}
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        print(f)
        
        for k, v in f.items():
            if v > len(nums)/2:
                return k
        
