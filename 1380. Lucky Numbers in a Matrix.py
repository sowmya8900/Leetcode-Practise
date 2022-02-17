class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ln = []
        '''for i in range(len(matrix)):
            l = []
            ind = matrix.index(min(matrix[i]))
            if(all(matrix[i][ind] > ))'''
        flag = 1
        for i in range(len(matrix)):
            x = min(matrix[i])
            ind = matrix[i].index(x)
            for j in range(len(matrix)):
                if(x >= matrix[j][ind]):
                    #ln.append(min(i))
                    flag = 0
                else:
                    flag = 1
                    break
            if flag == 0:
                ln.append(x)
        return(ln)
