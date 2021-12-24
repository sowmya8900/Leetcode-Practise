class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s = ""
        for i in range(len(nums)):
            s = s + str(nums[i])
            n = int(s, 2)
            #print(s, n)
            
            if n%5 == 0:
                nums[i] = True
            
            else:
                nums[i] = False
        return nums
