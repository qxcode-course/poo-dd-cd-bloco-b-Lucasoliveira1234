class Camisa:
    def __init__(self):
        self .__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str): 
        tamanhosValidos = ["PP", "P", "M", "G", "GG", "XG"]
        valor = valor.strip().upper()

        if valor in tamanhosValidos:
            self.__tamanho = valor
            return True
        else:
            print(f"Tamanho inválido!")
            return False
        
def main():
    roupa = Camisa()

    while roupa.getTamanho() == "":
        print("Digite seu tamanho de roupa")
        tamanho = input()
        if roupa.setTamanho(tamanho):
            print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())
            break

main()