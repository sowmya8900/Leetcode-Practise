class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = []
        c = 0
        for i in nums:
            if i == 1:
                c += 1
            
            if i == 0:
                l.append(c)
                c = 0
        l.append(c)
        return(max(l))
        
