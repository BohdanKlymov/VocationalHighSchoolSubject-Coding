class Pizza_Dough:
    def __init__(self, gramFlour: int, gramYeast: int, mlWater: int, gramSalt: int):
        self.gramFlour = gramFlour
        self.gramYeast = gramYeast
        self.mlWater = mlWater
        self.gramSalt = gramSalt

    def setFlour(self, neu_flour: int):
        self.gramFlour = neu_flour

    def setYeast(self, neu_yeast: int):
        self.gramYeast = neu_yeast

    def setWater(self, neu_water: int):
        self.mlWater = neu_water

    def setSalt(self, neu_salt: int):     
        self.gramSalt = neu_salt

    def getTeigGewichtInGramm(self) -> int:
    return self.gramFlour + self.gramYeast + self.mlWater + self.gramSalt

    def getTeigGewichtInKilo(self) -> float:
    return self.getTeigGewichtInGramm() / 1000              

    def fuegeMehlHinzu(self, menge: int):
    self.gramFlour += menge