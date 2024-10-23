class Animal:
    alive = True #Живой
    fed = False  #Накормленный
    def __init__(self, name):
        self.name = name #индивидуальное название каждого животного.



class Plant:
    edible = False #съедобность
    def __init__(self, name):
        self.name = name



class Mammal (Animal):
    def eat(self, food):  #метод, где food - это параметр, принимающий объекты классов растений
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.fed = False
            self.alive = False


class Predator (Animal):
    def eat(self, food):
        if food.edible == True:  #метод, где food - это параметр, принимающий объекты классов растений
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.fed = False
            self.alive = False


class Flower (Plant):
    edible = False
    pass


class Fruit (Plant):
    edible = True
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

