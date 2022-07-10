class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        '''for i in range(0, len(arr)-1):
            if arr[i] == 0:
                t = arr[i+1]
                arr[i+1] = arr[i]'''
        
        i = 0
        while(i < len(arr)):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                #print(arr)
                arr.pop()
                #print(arr)
                i += 1
            i += 1
