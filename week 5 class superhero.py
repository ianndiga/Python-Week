# Assignment 1: Design Your Own Class! 
class Superhero:
    def __init__(self, name, superpower, strength, weakness):
        self.name = name         
        self.superpower = superpower  
        self.strength = strength      
        self.weakness = weakness     
    
    def use_superpower(self):
        return f"{self.name} uses {self.superpower}!"

    def display_info(self):
        return (f"Superhero: {self.name}\n"
                f"Superpower: {self.superpower}\n"
                f"Strength: {self.strength}\n"
                f"Weakness: {self.weakness}")
    
    def fight(self):
        return f"{self.name} is fighting evil with {self.superpower}!"
class FlyingSuperhero(Superhero):
    def __init__(self, name, superpower, strength, weakness, flight_speed):
        
        super().__init__(name, superpower, strength, weakness)
        self.flight_speed = flight_speed  
    
    def use_superpower(self):
    
        return f"{self.name} soars through the sky at {self.flight_speed} km/h using {self.superpower}!"
    
    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"



class InvisibilitySuperhero(Superhero):
    def __init__(self, name, superpower, strength, weakness, duration):
        
        super().__init__(name, superpower, strength, weakness)
        self.duration = duration  
    
    def use_superpower(self):
        
        return f"{self.name} becomes invisible for {self.duration} seconds using {self.superpower}!"
    
    def sneak(self):
        return f"{self.name} sneaks past the enemy while invisible."

hero1 = Superhero("Captain Justice", "super strength", 95, "water")
hero2 = FlyingSuperhero("Sky Avenger", "flight", 80, "kryptonite", 300)
hero3 = InvisibilitySuperhero("Shade", "invisibility", 60, "sound", 30)

print(hero1.display_info())
print(hero1.fight())
print(hero1.use_superpower())

print("\n")

print(hero2.display_info())
print(hero2.fly())
print(hero2.use_superpower())

print("\n")

print(hero3.display_info())
print(hero3.sneak())
print(hero3.use_superpower())


# Activity 2: Polymorphism Challenge!
# Base class for animals and vehicles
class MovingObject:
    def move(self):
        pass 

class Car(MovingObject):
    def move(self):
        print("Driving")

class Plane(MovingObject):
    def move(self):
        print("Flying")

class Dog(MovingObject):
    def move(self):
        print("Running")

class Fish(MovingObject):
    def move(self):
        print("Swimming")

def demonstrate_movement(moving_objects):
    for obj in moving_objects:
        obj.move()

car = Car()
plane = Plane()
dog = Dog()
fish = Fish()

objects = [car, plane, dog, fish]

demonstrate_movement(objects)
