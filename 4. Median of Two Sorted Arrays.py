class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        l = sorted(nums1)
        print(l)
       
        if len(l) % 2 != 0:
            ind = ((len(l)+1)//2)-1
            median = l[ind]
        
        if len(l) % 2 == 0:
            ind1 = (len(l)//2)-1
            ind2 = ind1 + 1
            median = (l[ind1] + l[ind2])/2
            
        return(median)
        
        
