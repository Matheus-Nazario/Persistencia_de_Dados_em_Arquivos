# ler arquivo binário

import pickle


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# abre o arquivo
arquivo = open("exemploarquivobinario", "rb")  # read bytes

# carrega o conteudo do arquivo para a variavel p
# (nesse exemplo, o arquivo contem um objeto da classe Pessoa)
# é necessáro que a classe esteja implementada no programa
p = pickle.load(arquivo)

print(p.nome)
print(p.idade)

arquivo.close()
