class Human:
    def __init__( self, name="", age=0 ):
        self.name = name
        self.age = age

@property
def name(self):
    return self._name

@property
def age(self):
    return self._age


@property
def name(self):
    return self._name

@name.setter
def name(self, name: str):
    print("calling the setter")
    if name.islower():
        raise ValueError("Name cannot be all lower case")
    self._name = name

@age.setter
def age(self, age: int):
    print("set your age")
    self._age = age

@name.deleter
def name(self):
    print("deleting...")
    del self._name

@age.deleter
def __set__(self):
    print("deleting age.....")


nk = Human
nk.age = 50
print(f"nk is {nk.age} years old")
