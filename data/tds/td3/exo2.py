def square(num):
    return num**2

print("Valeur carrée de 1 à 10")
for i in range(0, 11):
    print(f"Carré de {i} = {square(i)}")

def absolute_value(num):
    return abs(num)

def absolute_cube(num):
    return square(absolute_value(num))

print("\nValeur Carré Absolu de -5 à 5")
for i in range(-5, 6):
    print(f"Carré absolu de {i} = {absolute_cube(i)}")