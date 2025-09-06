num = int(input("Ingresa un numero entero: "))
signo = -1 if num <0 else 1

numero_abs = abs(num)

invertido = 0

while numero_abs > 0:
    digito = numero_abs % 10
    invertido = invertido * 10 + digito
    numero_abs = numero_abs // 10

invertido *= signo

print(f"El numero invertido es: {invertido}")