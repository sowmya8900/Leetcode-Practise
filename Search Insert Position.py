class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(nums[len(nums)-1] < target):
            return(len(nums))
        for i in range(0, len(nums)):
            if(nums[i] >= target):
                return(i)
            
                
        
