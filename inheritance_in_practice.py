class Human(object):
    def __int__(self, first_name: str, last_name: str, age: int, sex: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

        def full_name(self):
            return f"{self.last_name} {self.first_name}"


        def __str__(self):
            return f"name = {self.last_name} {self.first_name}, age = {self.age}, sex ={self.sex}"
