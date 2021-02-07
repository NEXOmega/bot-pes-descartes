"""
La fonction nous donne le nombre de  7 dans un nombre 
"""

def div7(n):
    num = 0
    while n > 7:
        if n % 7 == 0:
            num = num + 1
        n = n - 1
    return num

print(div7(42))
