class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i = i.reverse()
        
        for i in image:
            for j in range(len(i)):
                if i[j] == 1:
                    i[j] = 0
                elif i[j] == 0:
                    i[j] = 1
            
        return(image)
