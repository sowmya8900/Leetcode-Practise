class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f = {}
        for i in arr:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        print(f)
        if len(list(f.values())) != len(set(f.values())):
            return False
        return True
