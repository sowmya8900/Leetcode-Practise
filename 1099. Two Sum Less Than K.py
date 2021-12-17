class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        l = []
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s < k:
                    l.append(s)
        
        if len(l) != 0:
            return max(l)
        return -1
