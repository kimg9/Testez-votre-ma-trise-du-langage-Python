## Écrivez votre code ici !
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return print(f"Nom : {self.name} \nAge: {self.age}")

  
class Employee(Person):
    def __init__(self, salary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.salary = salary

    def display_details(self):
        super().display_details()
        return print(f"Salaire : {self.salary}")

Employee(name="John",age=27,salary=35000).display_details()