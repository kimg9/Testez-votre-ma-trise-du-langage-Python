# ## Écrivez votre code ici !
# def square(number):
#     if isinstance(number, int) or isinstance(number, float):
#         return number * number
#     else:
#         print(f"Erreur ! {number} n'est pas un nombre !")
#         return None

def square(number):
    try:
        return number * number
    except TypeError:
        print(f"Erreur ! {number} n'est pas un nombre !")
        return None

print(f"The square root of {25} is: {square(25)}")
print(square("abc"))
