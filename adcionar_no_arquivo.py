# adicionar conteudo em arquivo de texto

arquivo = open("arquivo.txt", "a")          # append

arquivo.write("\nEssa linha será adicionada no final do arquivo")
arquivo.write("\nEscreve outra linha")

arquivo.close()
