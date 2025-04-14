#1. Assignment 1: Designing Own Class

class FootballPlayer:
    def __init__(self, name, position, stamina, skill_level):
        self.name = name
        self.position = position
        self.stamina = stamina
        self.skill_level = skill_level

    def play(self):
        print(f"{self.name}, the {self.position}, plays with skill level {self.skill_level} and stamina {self.stamina}.")

# Subclass with inheritance and encapsulation
class Goalkeeper(FootballPlayer):
    def __init__(self, name, stamina, skill_level, clean_sheets):
        super().__init__(name, "Goalkeeper", stamina, skill_level)
        self.__clean_sheets = clean_sheets 

    def play(self):
        # Polymorphism — overriding the base method
        print(f"{self.name} defends the goal fiercely! Clean sheets this season: {self.__clean_sheets}")

    def get_clean_sheets(self):
        return self.__clean_sheets

    def set_clean_sheets(self, new_count):
        if new_count >= 0:
            self.__clean_sheets = new_count
        else:
            print("Clean sheets count must be non-negative.")

# Creating objects
player1 = FootballPlayer("Lionel Messi", "Forward", 85, 95)
player2 = Goalkeeper("Manuel Neuer", 90, 92, 15)

player1.play()
player2.play()












# 2.Polymorphism Challenge! 🎭

class Vehicle:
    def move(self):
        print("The vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road! 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky! ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the path! 🚲")

# Polymorphism in action
vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()
