class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = [0]
        for i in ops:
            if i.lstrip('-').isdigit():
                s.append(int(i))
            
            elif(i == '+'):
                s.append(sum(s[-2:]))
                
            elif(i == 'D'):
                s.append(2*s[-1])
            
            elif(i == 'C'):
                s.pop()
        print(s)
        return(sum(s))
