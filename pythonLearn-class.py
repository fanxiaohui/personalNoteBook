# "with" statement call flow:  __init__  ,   __enter__  ,   __exit__

class CountFromBy():
    def __init__(self, start:int = 0, step:int = 1) -> None:
        self.num = start
        self.step = step
        print('init')
        
    def increase(self) -> None:
        self.num += self.step

    def __enter__(self) :
        print('enter')
        return CountFromBy(step=15)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        print('exit')
        

if __name__ == '__main__':
    with CountFromBy() as c:  # c is return value of __enter__
        c.increase()
        print(c.num)
    
    
    
///////////////////output:
init
enter
init
15
exit
