class Animal:
    def __init__(self, animal):
        print(animal, 'is an animal')


class Mammal(Animal):
    def __init__(self, mammal):
        print(Mammal, 'is a warm blooded animal')
        super().__init__(Mammal)

class NonWingedMammal(Mammal):
     def __init__(self, nonwingedmammal):
        print(nonwingedmammal, 'cant fly')
        super().__init__(nonwingedmammal)


class NonMarineMammal(Mammal):
     def __init__(self, nonmarinemammal):
        print(nonmarinemammal, 'cant swim')
        super().__init__(nonmarinemammal)

class Dog(NonMarineMammal,NonWingedMammal):
     def __init__(self):
        print('dog has 4 legs')
        super().__init__('dog')        

dog1 = Dog()





    