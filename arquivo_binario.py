# criar arquivo binário

import pickle


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# cria o objeto
pessoa1 = Pessoa("Paulo", 30)

# cria o arquivo binário
arquivo = open("exemploarquivobinario", "wb")  # write bytes

# armazena objeto no arquivo
pickle.dump(pessoa1, arquivo)

arquivo.close()
