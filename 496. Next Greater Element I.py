class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in nums1:
            ind = nums2.index(i)
            for j in range(ind, len(nums2)):
                ele = -1
                if nums2[j] > nums2[ind]:
                    ele = nums2[j]
                    break
            l.append(ele)
        return(l)
