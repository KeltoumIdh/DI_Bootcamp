#Exercise 1 :
print("Exercise 1 : ")#pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#Create the siamese class
class Siamese(Cat):
    pass

#Create a list of cat instances
bengal_obj = Bengal("Simba", 3)
chartreux_obj = Chartreux("Luna", 5)
siamese_obj = Siamese("Milo", 2)

all_cats= [bengal_obj,chartreux_obj,siamese_obj]

#Create a pets instance
sara_pets = Pets(all_cats)

#Take cats for a walk
sara_pets.walk()

#Exercise 2
print("Exercise 2 : ") #Dogs

class Dog():

    def __init__(self,dog_name,dog_age,dog_weight):
        self.dog_name = dog_name
        self.dog_age = dog_age
        self.dog_weight = dog_weight

    def bark(self):
        print(f'{self.dog_name} is barking')

    def run_speed(self):
        return self.dog_weight/self.dog_age*10

    def fight(self,other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f"{self.dog_name} won")
        else :
            print(f"{other_dog.dog_name} won")

#Create dog instance:
dog1 = Dog("Fido", 4, 12)
dog2 = Dog("Bella", 2, 8)
dog3 = Dog("Max", 6, 20)

dog3.bark()
print(f'{dog2.dog_name} run speed is {dog2.run_speed()}')
dog1.fight(dog2)

#Exercise 3
print('Exercise 3 : ')

import random

class PetDog(Dog):
    def __init__(self,dog_name,dog_age,dog_weight,trained = False):
        super().__init__(dog_name,dog_age,dog_weight)
        self.trained =trained

    def train(self):
        self.bark()
        self.trained=True

    def play(self, *args):
        # Collect all dog names (including this dog)
        dog_names = [self.dog_name] + [dog for dog in args]
        print(f"{', '.join(dog_names)} all play together!")

    def do_a_trick(self):
         if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.dog_name} {random.choice(tricks)}")


my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

#Exercise 4 :
print("Exercise 4 : ")#Family and perso, classes

class Person:
    def __init__(self,first_name,age,last_name=[]):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        if self.age >= 18 :
            return True
        else:
            return False


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []  # store Person objects

    def born(self,first_name,age):
        new_born = Person(first_name,age,self.last_name)
        self.members.append(new_born)
        return new_born

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("No family member found with that name.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")
        for person in self.members:
            print(f"{person.first_name}, age {person.age}")

# Create a family
my_family = Family("Smith")
my_family.born("Alice", 17)
my_family.born("Bob", 20)

# Check majority
my_family.check_majority("Alice")  # ➜ Sorry...
my_family.check_majority("Bob")    # ➜ You are over 18...

# Presentation
my_family.family_presentation()