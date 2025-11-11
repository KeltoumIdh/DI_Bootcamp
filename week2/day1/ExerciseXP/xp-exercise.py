from itertools import groupby


# Exercise 1: Cats
print('**** exercise 1 ****')
class Cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age

cat1=Cat('cat1',6)
cat2=Cat('cat2',10)
cat3=Cat('cat3',2)
def find_old(cat1, cat2, cat3):
    oldest_cat = max([cat1, cat2, cat3], key=lambda cat: cat.age)
    return oldest_cat

oldest = find_old(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is  {oldest.age} years old")

#Exercise 2 : Dogs
print('*********exo2*********')
class Dog():
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def bark(self):
        print(f'{self.name} goes woof')
    def jump(self):
        print(f'{self.name} jumps {self.height*2} cm high!')

davids_dog=Dog('dv',20)
sarahs_dog =Dog('sr',60)
print(f'name:{davids_dog.name},{sarahs_dog.name} age:{davids_dog.height},{sarahs_dog.height} ')
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

#🌟 Exercise 3 : Who’s the song producer?

print('*********exo3*********')
class Song():
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
            print(*self.lyrics)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

#🌟 Exercise 4 : Afternoon at the Zoo


print('*********exo4*********')
class Zoo():
    animals=[]
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if isinstance(animal, str) and ',' in animal:
                for a in [x.strip() for x in animal.split(',') if x.strip()]:
                    if a not in self.animals:
                        self.animals.append(a)
                    else:
                        print(f"{a} already exists")
            else:
                if animal not in self.animals:
                    self.animals.append(animal)
                else:
                    print(f"{animal} already exists")

    def get_animals(self):
        print(self.animals)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        sorted_animals=sorted(self.animals)
        grouped_by_first_letter = []
        for first_char, group_iter in groupby(sorted_animals, key=lambda word: word[0]):
            grouped_by_first_letter.append((first_char, list(group_iter)))
        return grouped_by_first_letter

    def get_groups(self):
        grouped_by_first_letter = self.sort_animals()
        for k, v in grouped_by_first_letter:
            print(f"{k}: {v}")

brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("g,k,l")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()


