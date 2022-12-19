class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l =[]
        maxc = max(candies)
        for i in candies:
            print(i + extraCandies, maxc)
            if (i + extraCandies) >= maxc:
                l.append(True)
            else:
                l.append(False)
        return l
