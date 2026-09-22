Class Player:
    def __init__(self, name: str, points: int, level: int):
        self.name = name
        self.points = points
        self.level = level

    def setName(self, neu_name: str):
        self.name = neu_name

    def getName(self):
        return self.name

    def pointsUp(self, amount: int):
        if amount > 0:
            self.points += amount
        else:
            print("Points increase must be positive.")

    pointDown(self, amount: int):
        if amount > 0 and amount <= self.points:
            self.points -= amount        

    def getPoints(self):
        return self.points

    def getLevel(self):
        return self.level