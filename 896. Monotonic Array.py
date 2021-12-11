class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if(all(nums[x] <= nums[x+1] for x in range(0, len(nums)-1))):
            return True
        elif(all(nums[x] >= nums[x+1] for x in range(0, len(nums)-1))):
            return True
        else:
            return False
        
