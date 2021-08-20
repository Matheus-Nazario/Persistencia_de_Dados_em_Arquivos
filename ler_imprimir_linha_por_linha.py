# ler arquivo de texto linha por linha

arquivo = open("arquivo.txt", "r")

for linha in arquivo:  # percorre o arquivo
    print(linha)  # implime cada linha

arquivo.close()
