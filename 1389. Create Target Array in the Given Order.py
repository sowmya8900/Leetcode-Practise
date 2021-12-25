class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l = []
        for i in range(0, len(nums)):
            l.insert(index[i], nums[i])
        return(l)
