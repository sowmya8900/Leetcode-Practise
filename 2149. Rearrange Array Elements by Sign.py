class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lp, ln = [], []
        l = []
        for i in nums:
            if i > 0:
                lp.append(i)
            else:
                ln.append(i)
        for i in range(0, len(lp)):
            l.extend([lp[i], ln[i]])
        return l
