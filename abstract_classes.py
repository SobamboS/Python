import abc

class Mammal(abc.ABC):
    pass
m1 = Mammal()
@abc.abstractmethod
def move(self):
    pass

class Person(Mammal):
    def move( self ):
        pass

p1 = Person()

print("hello" + 2)