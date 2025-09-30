class Carro:
    def __init__(self, passageiros: int):
        self.passageiros: int = passageiros
        self.passMax: int = 2
        self.gasMax: int = 100
        self.gas: int = 0
        self.km: int = 0 

    def __str__(self) -> str:
        return f"pass: {self.passageiros}, gas: {self.gas}, km: {self.km}"
        
    def enter (self):
        if self.passageiros >= self.passMax:
            print("fail: limite de pessoas atingido")
        else:
            self.passageiros+=1

    def leave (self):
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.passageiros-=1
        
def main():
    carro = Carro(0)
    while True:
        line: str = input()
        print(f"$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "show":
            print(carro)

        elif args[0] == "enter":
            carro.enter()

        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "end":
            break

main()