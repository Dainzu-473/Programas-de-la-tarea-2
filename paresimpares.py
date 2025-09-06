n = int(input("Ingresa un numero entero n: "))

suma_pares = 0
suma_impares = 0

for i in range (1, n+1):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print(f"Suma de los numeros pares {n}: {suma_pares}")
print(f"Suma de los numeros impares {n}: {suma_impares}")