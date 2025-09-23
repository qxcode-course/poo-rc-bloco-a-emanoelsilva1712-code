class Towel:
    #construtor
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    #aumentar a umidade da toalha.
    def dry(self, amount: int):
        max_wetness = self.get_max_wetness()
        new_wetness = self.wetness + amount

        #valor máximo da umidade
        if new_wetness > max_wetness:
            self.wetness = max_wetness
            print("A toalha está completamente encharcada!")
        else:
            self.wetness = new_wetness
            print(f"A toalha agora tem {self.wetness} de umidade.")

    #torcer a toalha e zerar a umidade
    def wring_out(self):
        self.wetness = 0
        print("Você torceu a toalha. Ela agora está seca.")

    #retorna o valor máximo de umidade
    def get_max_wetness(self) -> int:
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30
        else:
            #se o tamanho não for P, M ou G
            print("Tamanho de toalha inválido, retornando 0.")
            return 0

    #verifica se a toalha está seca
    def is_dry(self) -> bool:
        return self.wetness == 0