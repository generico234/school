b = input("Ingrese un numero binario: ")
dec = 0
pot = 1
ind = len(b) - 1
while ind >= 0:
    if b[ind] == "1":
        dec = dec + pot
    pot = pot * 2
    ind = ind - 1
print("El numero decimal es:", dec)