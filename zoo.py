class Animal:
    def __init__(self, name, type, species, weight):
        self.name = name
        self.type = type
        self.species = species
        self.weight = weight

    def show_information(self):
        return f"Name: {self.name}, Type: {self.type}, Species: {self.species}, Weight: {self.weight}lb"

class Mammal(Animal):
    def __init__(self, name, species, weight, litterSize):
        super().__init__(name, "Mammal", species, weight)
        self.litterSize = litterSize

    def show_information(self):
        return super().show_information() + f", LitterSize: {self.litterSize}"

class Reptile(Animal):
    def __init__(self, name, species, weight, venomous):
        super().__init__(name, "Reptile", species, weight)
        self.venomous = venomous

    def show_information(self):
        venomous_text = "Yes" if self.venomous else "No"
        return super().show_information() + f", Venomous: {venomous_text}"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        print("Animal List:")
        for animal in self.animals:
            print(f"Animal Detail: {animal.show_information()}")
            
jackson = Animal("Jackson", "mammal", "gat", 13)
jacksonMammal = Mammal("Jackson", "gat", 13, 2)
cocodrilo = Reptile("coco", "cocodrilo", 40, False)
# print(f"""
#       DATOS: \n\n
#       Nombre: {tita.name} \n
#       Tipo: {tita.type} \n
#       Especie: {tita.species} \n
#       Peso: {tita.weight} 
#       """)

print(cocodrilo.show_information())
#se crea una instancia de la clase zooo
my_zoo = Zoo()
# my_zoo.add_animal(cocodrilo)
# my_zoo.add_animal(jackson)
my_zoo.list_animals()
