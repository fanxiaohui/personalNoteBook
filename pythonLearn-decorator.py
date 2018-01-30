
#decorator: 1) a decorator is a function; 2)input a function, output a new function;3)keep the same function signature


def apply(func: object, *value) -> object: #outer is a decorator
    return func(*value)


def outer(*args) -> object:  
    def inner(word:str):
        print(*args, word)    
    return inner
    

if __name__ == '__main__':    
    f = apply(outer,1,2)
    f('hello')
    
    
///////////output:
1 2 hello
