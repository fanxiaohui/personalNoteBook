#__enter__ , __exit__ is to support "with" statement, they are optional

class CountFromBy():
    def __init__(self, start:int = 0, step:int = 1):
        self.num = start
        self.step = step
        
    def increase(self) -> None:
        self.num += self.step

    def __enter__(self) -> None:        
        pass

    def __exit__(self) -> None:
        pass        
        
if __name__ == '__main__':
    c = CountFromBy(step=15)
    for i in range(3):
        c.increase()
    print(c.num) #45
    
    
