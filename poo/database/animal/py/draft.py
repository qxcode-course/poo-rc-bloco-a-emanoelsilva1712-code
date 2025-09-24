class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __str__(self) -> str:
        return f"{self.species}: {self.sound}: {self.age}"
    


def main():
    animal: Animal = Animal("","")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str]
    