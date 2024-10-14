words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

final_list = []
for word in words:
    count = 0
    for letter in word:
        if  letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            count += 1
    final_list.append((word, count),) 
    
# list_tuples = [(word, sum(1 for letter in word if letter in 'aeiouAEIOU')) for word in words]

print(final_list)