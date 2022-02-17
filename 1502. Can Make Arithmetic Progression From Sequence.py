class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if arr != sorted(arr):
            arr = sorted(arr)
        print(arr)
        
        d = arr[0] - arr[1]
        
        for i in range(len(arr)-1):
            d_dash = arr[i] - arr[i+1]
            if d != d_dash:
                return False
        return True
