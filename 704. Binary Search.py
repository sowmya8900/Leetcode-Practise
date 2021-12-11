class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums)-1
        mid = (beg + end)//2
        
        if target not in nums:
            return -1
        
        while(nums[mid] != target):
            
            if(nums[mid] < target):
                beg = mid+1
            
            if(nums[mid] > target):
                end = mid-1
           
            mid = (beg + end)//2
            
        return mid
