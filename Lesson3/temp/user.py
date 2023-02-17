class User:
    age = 1;

    def __init__(self, name):
        print("Hi world")
        self.username = name
        
    def sayName(self):
        print("My name is", self.username)
    
    def sayAge(self):
        print(self.age)
    
    def satAge(self, newAge):
        self.age = newAge

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card