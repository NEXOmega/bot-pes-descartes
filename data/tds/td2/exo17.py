import random
import math
nbr = []
nbr_iter = int(input("Nombre d'itérations : "))

for i in range(0, nbr_iter):
    nbr.append(random.random())

def moy_from_list(list):
    moy = 0
    for nb in list:
        moy += nb
    return moy/len(list)

def ecart_type_from_list(list, moy):
    ecart_type = 0
    for nb in list:
        ecart_type += nb**2
    return math.sqrt(ecart_type/moy)

moyenne = moy_from_list(nbr)
print(f"Moyenne : {moyenne}, Ecart Type : {ecart_type_from_list(nbr, moyenne)}")
