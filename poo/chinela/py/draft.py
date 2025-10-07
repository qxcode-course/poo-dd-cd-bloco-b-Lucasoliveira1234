class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        if valor % 2 == 0 and 20 <= valor <= 50:
            self.__tamanho = valor
            return True
        else:
            return False

def main():
    chinela = Chinela()

    while chinela.getTamanho() == 0:
        tamanho:int = int(input("Digite um tamanho válido"))

        if chinela.setTamanho(tamanho):
            print("Tamanho", chinela.getTamanho(), "Registrado com sucesso")
            break

        else:
            print("Valor inválido! O tamanho deve ser PAR entre 20 e 50.")

main()

