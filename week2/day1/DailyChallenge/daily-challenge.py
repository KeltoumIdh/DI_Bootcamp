# Old MacDonald’s Farm
class Farm():
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, **kwargs):
        for animal_type, count in kwargs.items():
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_list = []
        for animal in animal_types:
            count = self.animals[animal]
            if count > 1:
                animal_list.append(f"{animal}s")
            else:
                animal_list.append(animal)

        if len(animal_list) == 0:
            return f"{self.name}'s farm has no animals."
        elif len(animal_list) == 1:
            return f"{self.name}'s farm has {animal_list[0]}."
        elif len(animal_list) == 2:
            return f"{self.name}'s farm has {animal_list[0]} and {animal_list[1]}."
        else:
            return f"{self.name}'s farm has {', '.join(animal_list[:-1])} and {animal_list[-1]}."

    def get_info(self):
        output = f"{self.name}'s farm\n"
        if self.animals:
            max_animal_len = max(len(animal) for animal in self.animals)
        else:
            max_animal_len = 0
        for animal, count in self.animals.items():
            output += f"{animal.ljust(max_animal_len)} : {str(count).rjust(3)}\n"
        output += "E-I-E-I-0!"
        return output

macdonald = Farm("McDonald")
macdonald.add_animal(cow=5, sheep=2, goat=12)
print(macdonald.get_info())
print(macdonald.get_short_info())