import numpy as np

students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

name = input("Entrez le nom de l’étudiant :  ")

if name in students:
     print(f"Notes de {name}")
     for key , value in students[name].items():
          print(f"{key} : {value}")
     mean = round(np.array(list(students[name].values())).mean(), 2)
     print(f"Moyenne de {name} : {mean}")
else:
     print(f"L'étudiant {name} n'existe pas dans la liste.")