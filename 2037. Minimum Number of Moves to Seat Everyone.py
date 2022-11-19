class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        s = 0
        seats = sorted(seats)
        students = sorted(students)
        #print(seats, students)
        for i in range(0, len(seats)):
            s += abs(seats[i] - students[i])
        return(s)
