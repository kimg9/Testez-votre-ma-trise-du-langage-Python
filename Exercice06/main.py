import numpy as np

# Fonction calculate_average
def calculate_average(numbers):
    return round(np.array(numbers).mean(), 2)
 
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
