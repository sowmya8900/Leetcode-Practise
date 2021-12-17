class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[len(arr)-1] - arr[0])/len(arr)
        #print(d)
        if all(arr[x] == arr[x+1] for x in range(len(arr)-1)):
            return arr[0]
        for i in range(len(arr)):
            if (arr[i+1]-arr[i]) != d:
                return int(arr[i]+d)
