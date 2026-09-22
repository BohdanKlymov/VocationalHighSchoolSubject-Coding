class Rectangle:

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def setLength(self, neu_length: float):
        self.length = neu_length

    def setWidth(self, neu_width: float):
        self.width = neu_width

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getArea(self, area: float):
        area = self.length * self.width
        return area

    def getScope(self, scope: float):
        scope = 2 * (self.length + self.width)
        return scope    

