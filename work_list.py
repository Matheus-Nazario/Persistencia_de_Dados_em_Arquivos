# ------- arquivo_um pergunta -----
arquivo_um = open("arquivo_um.txt", "w")

for i in range(5):
    n = int(input("arquivo_um - Digite um número: "))
    arquivo_um.write(str(n) + "\n")

arquivo_um.close()

# ------- arquivo_dois pergunta -----

arquivo_dois = open("arquivo_dois.txt", "w")

for i in range(6):
    n = int(input("arquivo_dois - Digite um número: "))
    arquivo_dois.write(str(n) + "\n")

arquivo_dois.close()

# ---------lista -------------

lista_do_arquivo = []

# ------- arquivo_um lista -----
arquivo_um = open("arquivo_um.txt", "r")

for linha in arquivo_um:
    num = int(linha)
    lista_do_arquivo.append(num)

arquivo_um.close()

# ------- arquivo_dois lista -----

arquivo_dois = open("arquivo_dois.txt", "r")

for linha in arquivo_dois:
    num = int(linha)
    lista_do_arquivo.append(num)

arquivo_dois.close()

# ------  colocando a lista em ordek crente
lista_ordem = sorted(lista_do_arquivo)

# arquivo de saída em ordem------
arquivo_de_saida = open("arquivo_de_saida.txt", "w")

for i in lista_ordem:
    n = str(i)
    arquivo_de_saida.write(n + "\n")

arquivo_de_saida.close()
