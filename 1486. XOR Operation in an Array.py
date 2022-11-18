class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2*i)
        #print(nums)
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        return(xor)
