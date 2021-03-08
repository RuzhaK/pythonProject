class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species=="mammal":
            self.mammals.append(name)
        elif species=="fish":
            self.fishes.append(name)
        elif species=="bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        zoo_name=self.name
        if species=="mammal":
            species_names=self.mammals
            species="mammals"
        elif species=="bird":
            species_names=self.birds
            species="birds"
        elif species=="fish":
            species_names=self.fishes
            species=="fishes"
        species=species.capitalize()
        names=', '.join(species_names)

        # todo greshni skriti testove
        return f"{species} in {zoo_name}: {names}"

    def get_total(self):
        return f"Total animals: {self.__animals}"

zoo_name = input()
zoo=Zoo(zoo_name)
n = int(input())

for i in range(n):
    species, name = input().split()
    zoo.add_animal(species,name)

species = input()

print(zoo.get_info(species))
print(zoo.get_total())