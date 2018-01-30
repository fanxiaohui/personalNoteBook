
#decorator: 1) a decorator is a function; 2)input a function, output a new function;3)keep the same function signature


def apply(func: object, *value) -> object: #apply is a decorator
    return func(*value)


def outer(*args) -> object:  
    def inner(*inargs):
        print(*args, *inargs)    
    return inner #note: don't return inner()
    

if __name__ == '__main__':    
    f = apply(outer,1,2)
    f('hello','world')
    
    
///////////output:
1 2 hello world
