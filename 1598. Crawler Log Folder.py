class Solution:
    def minOperations(self, logs: List[str]) -> int:
        l = []
        for log in logs:
            if log[-1] == '/' and log[-2] != '.':
                l.append(log)
            if log == './':
                pass
            if log == '../':
                if l:
                    l.pop()
        return(len(l))
