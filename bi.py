numero_decimal = int(input("Ingresa un número decimal: "))

original = numero_decimal

binario = ""

if numero_decimal == 0:
    binario = "0"

while numero_decimal > 0:
    residuo = numero_decimal % 2
    binario = str(residuo) + binario
    numero_decimal = numero_decimal // 2

print("El número", original, "en binario es", binario)