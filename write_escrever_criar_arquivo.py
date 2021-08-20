# criar arquivo de texto

# O arquivo é criado no diretório do programa
# Se o arquivo já existe, será sobrescrito
arquivo = open("arquivo02.txt", "w")  # write

arquivo.write("Escreve uma linha\n")  # \n para pular as linhas
arquivo.write("Escreve outra linha\n")
arquivo.write(str(1.30))  # converte numeros para string
arquivo.write("\n")

a = 100
arquivo.write(str(a))  # escreve o conteudo de uma variável

arquivo.close()  # fecha o arquivo
