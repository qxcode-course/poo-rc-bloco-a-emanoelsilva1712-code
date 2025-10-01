class Calc:
    def __init__(self, batteryMax: int):
        self.display: int = 0
        self.battery: int = 0
        self.batteryMax: int = batteryMax

    def __str__(self) -> str:
        return f"display: {self.display:.2f}, battery: {self.battery}"
    
    def charge (self):
    
     