numero = int(input("Ingresa un numero entero: "))
numero_abs = abs(numero)

contador = 0

if numero_abs == 0:
    contador = 1
else:
    while numero_abs > 0:
        numero_abs = numero_abs // 10
        contador += 1

print(f"El numero {numero} tiene {contador} digitos. ")
