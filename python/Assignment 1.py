class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, and I protect {self.city} with my {self.power}!")

    def attack(self):
        print(f"{self.name} uses {self.power} to fight evil!")

class FlyingHero(Superhero):
    def __init__(self, name, power, city, wingspan):
        super().__init__(name, power, city)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} soars through the skies with a wingspan of {self.wingspan} meters!")

class TechHero(Superhero):
    def __init__(self, name, power, city, gadget):
        super().__init__(name, power, city)
        self.gadget = gadget

    def use_gadget(self):
        print(f"{self.name} uses their {self.gadget} to save the day!")

hero1 = FlyingHero("Skyhawk", "Wind Control", "Airstorm", 15)
hero2 = TechHero("CyberKnight", "AI Combat", "TechCity", "laser drone")

hero1.introduce()
hero1.fly()
hero2.introduce()
hero2.use_gadget()
