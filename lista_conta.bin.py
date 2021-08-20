import pickle


class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo


arquivo = open("lista_conta.bin", "rb")
lista_conta = pickle.load(arquivo)

for c in lista_conta:
    print(f"Numero {c.numero}")
    print(f"Titular {c.titular}")
    print(f"Saldo {c.saldo}")
    print("---" * 10)


arquivo.close()
