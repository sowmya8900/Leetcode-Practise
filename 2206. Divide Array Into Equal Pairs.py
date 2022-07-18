class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            '''s = set(nums)
            #print(s)
            for i in s:
                if nums.count(i) % 2 != 0:
                    return False
            return True'''
            
            f = {}
            for i in nums:
                if i in f:
                    f[i] += 1
                else:
                    f[i] = 1
            for k, v in f.items():
                if v % 2 != 0:
                    return False
            return True
        return False
