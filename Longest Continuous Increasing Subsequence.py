class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        counts = [1]
        count = 1
        for i in range(0, len(nums)-1):
            
            if(nums[i] < nums[i+1]):
                count += 1
            
            else:
                count = 1
            counts.append(count)
                
        return(max(counts))
                
        #counts.append(count)
        
