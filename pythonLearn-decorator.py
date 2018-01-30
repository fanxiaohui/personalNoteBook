

def apply(func: object, *value) -> object:
    return func(*value)


def outer(*args) -> object:  #args is a tuple, could accept any number parameters
    def inner(word:str):
        print(*args, word)    
    return inner
    

if __name__ == '__main__':    
    f = apply(outer,1,2)
    f('hello')
    
    
///////////output:
1 2 hello
