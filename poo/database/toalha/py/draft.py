

class Towel: #Classe
    def __init__(self, color: str, size: str): #construtor
        self.color: str = color #atributo
        self.size: str = size
        self.wetness: int = 0

#referencia
print("Qual a cor da sua toalha e o tamanho?")
color = input()
size = input()
minha: Towel = Towel(color, size) #objeto
print(f"Sua toalha é {minha.color} e o tamanho é {minha.size}")




