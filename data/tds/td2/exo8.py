billets=[500,200,100,50,20,10,5,2,1]
somme = int(input("Somme : "))
"""
bil500 = somme//500
somme = somme%500
bil200 = somme//200
somme = somme%200
bil100 = somme//100
somme = somme%100
bil50 = somme//50
somme = somme%50
bil10 = somme//10
somme = somme%10
bil5 = somme//5
somme = somme%5
bil2 = somme//2
somme = somme%2
"""
nbr_bill = []
for i in [500,200,100,50,20,10,5,2,1]:
    bil = somme//i
    somme = somme%i
    print(bil)
    if(bil == 0):
        billets.remove(i)
    else:
        nbr_bill.append(f"{bil} * {i}")
print(" + ".join(nbr_bill))
