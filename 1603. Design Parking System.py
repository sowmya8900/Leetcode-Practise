class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.l = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.l[0] > 0:
                self.l[0] -= 1
                return True
        if carType == 2:
            if self.l[1] > 0:
                self.l[1] -= 1
                return True
        if carType == 3:
            if self.l[2] > 0:
                self.l[2] -= 1
                return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
