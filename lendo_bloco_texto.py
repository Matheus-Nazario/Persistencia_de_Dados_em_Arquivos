# ler arquivo de texto

# o arquivo já deve existir
# procura no diretório do programa
arquivo = open("arquivo.txt", "r")  # read

# copia o conteudo do arquivo para a variável a
# (uma única string com todo o conteudo do arquivo)
a = arquivo.read()

print(a)

arquivo.close()  # Fecha o arquivo
