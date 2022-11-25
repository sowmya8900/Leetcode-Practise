class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # s1 = " " * len(indices)
        # for i in range(0, len(indices)+1):
        #     s1 = s1[:indices[i]] + s[i] + s1[indices[i+1]:]
        # print(s1)

        s1 = ''
        for i in range(0, len(s)):
            s1 += s[indices.index(i)]
        return(s1)
