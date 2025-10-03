class Calc:
    def __init__(self, batteryMax: int):
        self.display: int = 0
        self.battery: int = 0
        self.batteryMax: int = batteryMax

    def __str__(self) -> str:
        return f"display: {self.display:.2f}, battery: {self.battery}"
    
    def charge (self, increment: int):
        self.battery+=increment
        if self.battery > self.batteryMax:

    def sum (self):
        if self.battery == 0:
            print("fail: bateria insuficiente")
        else:
            
    def div (self):
        if self.battery == 0:
            print("fail: bateria insuficiente")
        elif div == 0:
            print("fail: divisao por zero")
        else:
            
        
def main():
    calc = Calc()
    while True:
        line: str = input()
        print(f"$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "show":
            print(calc)

        if args[0] == "charge":
            increment = int(args[1])
            calc.charge(increment)

        if args[0] == "sum":
            calc.sum()

        if args[0] == "div":
            calc.div()

main ()