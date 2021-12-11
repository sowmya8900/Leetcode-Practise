class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        #l = [0] * len(nums)
        l = []
        #print(l)
        e, o = [], []
        for i in nums:
            if i%2 == 0:
                e.append(i)
            else:
                o.append(i)
        #print(e, o)
        for i in range(len(nums)):
            if i % 2 == 0:
                l.append(e[0])
                e.remove(e[0])
            if i % 2 != 0:
                l.append(o[0])
                o.remove(o[0])
        return(l)
