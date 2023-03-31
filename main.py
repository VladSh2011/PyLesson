class Cat:
    def __init__(self, name, age, host, breed):
        self.name = name
        if age > 20 or age < 0:
            self.__age = 3
        else:
            self.__age = age
        self.host = host
        self.__breed = breed
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age > 20 or age < 0:
            self.__age = 3
        else:
            self.__age = age
    @property
    def breed(self):
        return self.__breed
    
cat = Cat("Мурка", 4, "Ігор", "Дворова")
print(cat.age)
cat.age = 5
print(cat.age)
print(cat.breed)
