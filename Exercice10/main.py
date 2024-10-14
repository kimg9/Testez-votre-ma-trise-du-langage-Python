## Écrivez votre code ici !
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return print(f"Nom : {self.name} \nAge: {self.age}")

  
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        return print(f"Salaire : {self.salary}")

Employee("John",27,35000).display_details()
