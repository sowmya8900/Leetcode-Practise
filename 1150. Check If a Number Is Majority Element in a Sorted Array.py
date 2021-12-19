class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        f = {}
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        print(f)
        
        maj = len(nums)/2
        
        for k, v in f.items():
            if (v > maj) and (k == target):
                return True
        return False
