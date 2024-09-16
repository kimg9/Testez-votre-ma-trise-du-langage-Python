# Fonction calculate_average
def calculate_average(numbers: list):
    mean = 0
    for number in numbers:
        mean += number
    mean /= len(numbers)
    return mean
 
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
