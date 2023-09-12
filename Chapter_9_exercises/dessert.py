
class Dessert:
    def __init__(self, kindOfDessert, flavours):
        self.flavours = flavours
        self.kindOfDessert = kindOfDessert
    
    def response(self):
        return f"{self.kindOfDessert} with {self.flavours} is being process..."
    