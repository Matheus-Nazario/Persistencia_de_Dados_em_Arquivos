pares = open("pares.txt", "r")
impares = open("impares.txt", "r")

lista = []
for n in pares:
    lista.append(int(n))

for n in impares:
    lista.append(int(n))

print(lista)
lista.sort()
print(lista)

resultado = open("lista de numeros. txt", "w")
for n in lista:
    resultado.write(str(n) + "\n")

pares.close()
impares.close()
resultado.close()
