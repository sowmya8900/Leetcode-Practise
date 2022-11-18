class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # l = list(s.split())
        l = [int(x) for x in str.split(s) if x.isnumeric()]
        print(l)
        for i in range(0, len(l)-1):
            if l[i] >= l[i+1]:
                return False
        return True

        # for i in s:
        #     if i.isnumeric():
        #         l.append(int(i))
        # print(l)
