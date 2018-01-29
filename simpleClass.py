

class CountFromBy():
    def __init__(self, start:int = 0, step:int = 1):
        self.num = start
        self.step = step
        
    def increase(self) -> None:
        self.num += self.step

if __name__ == '__main__':
    c = CountFromBy(step=15)
    for i in range(3):
        c.increase()
    print(c.num) #45
    
    
