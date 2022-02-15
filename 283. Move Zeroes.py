class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        l = len(nums)
        for i in range(l):
            if nums[i] != 0:
                nums.insert(ind, nums[i])
                del nums[i+1]
                ind += 1
        print(nums)
