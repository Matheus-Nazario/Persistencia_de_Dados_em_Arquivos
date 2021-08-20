arquivo = open("ListaNumeros.txt", "r")

lista = []
for i in arquivo:
    lista.append(int(i))
    print(int(i))

soma = sum(lista)
print("Soma:", soma)

arquivo.close()
